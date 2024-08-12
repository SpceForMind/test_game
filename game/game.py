import pygame as pg
from os import path
import random

from game.constant import *
from game.player import Player
from game.mob import Mob
from game.input_box import InputBox
from game.explosion import Explosion
from game.pow import Pow


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def newmob():
    m = Mob()
    sprite_manager.all_sprites.add(m)
    sprite_manager.mobs.add(m)


def draw_shield_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)


def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)


def show_go_screen(player: Player):
    box = InputBox(WIDTH * 2 / 7, HEIGHT * 3 / 7, 140, 32)
    waiting = True
    records = sqlite_manager.get_scores()
    screen.blit(background, background_rect)
    draw_text(screen, 'Best', 22, WIDTH / 2, HEIGHT * 2 / 3)
    draw_text(screen, "Arrow keys move, Space to fire", 22,
              WIDTH / 2, HEIGHT / 4)

    shift = 30

    for r in records:
        draw_text(screen, f'{r[0]} - {r[1]}', 22, WIDTH / 2, HEIGHT * 2/ 3 + shift)
        shift += 30

    draw_text(screen, "Press Enter to begin", 18, WIDTH / 2, HEIGHT * 7 / 13)
    box.draw(screen)
    pg.display.flip()

    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False

            box.handle_event(event, player=player)
            box.update()
            screen.blit(background, background_rect)
            draw_text(screen, 'Best', 22, WIDTH / 2, HEIGHT * 2 / 3)
            shift = 30

            for r in records:
                draw_text(screen, f'{r[0]} - {r[1]}', 22, WIDTH / 2, HEIGHT * 2 / 3 + shift)
                shift += 30

            draw_text(screen, "Arrow keys move, Space to fire", 22,
                      WIDTH / 2, HEIGHT / 4)
            draw_text(screen, "Press Enter to begin", 18, WIDTH / 2, HEIGHT * 7 / 13)
            box.draw(screen)
            pg.display.flip()


def game_cycle():
    player = Player()
    sprite_manager.all_sprites.add(player)
    for i in range(8):
        newmob()
    score = 0

    # Цикл игры
    start_game = True
    game_over = False
    running = True

    while running:
        if start_game:
            if game_over:
                game_over = False
                sqlite_manager.insert(player_name=player.get_name(), score=score)

            show_go_screen(player=player)
            start_game = False
            sprite_manager.all_sprites = pygame.sprite.Group()
            sprite_manager.mobs = pygame.sprite.Group()
            sprite_manager.bullets = pygame.sprite.Group()
            sprite_manager.powerups = pygame.sprite.Group()
            player_name = player.get_name()
            player = Player()
            player.set_name(player_name)
            sprite_manager.all_sprites.add(player)
            for i in range(8):
                newmob()
            score = 0

        # Держим цикл на правильной скорости
        clock.tick(FPS)
        # Ввод процесса (события)
        for event in pygame.event.get():
            # проверка для закрытия окна
            if event.type == pygame.QUIT:
                running = False

        # Обновление
        sprite_manager.all_sprites.update()

        # проверьте, не попала ли пуля в моб
        hits = pygame.sprite.groupcollide(sprite_manager.mobs, sprite_manager.bullets, True, True)
        for hit in hits:
            score += 50 - hit.radius
            random.choice(expl_sounds).play()
            expl = Explosion(hit.rect.center, 'lg')
            sprite_manager.all_sprites.add(expl)
            if random.random() > 0.9:
                pow = Pow(hit.rect.center)
                sprite_manager.all_sprites.add(pow)
                sprite_manager.powerups.add(pow)
            newmob()

        #  Проверка, не ударил ли моб игрока
        hits = pygame.sprite.spritecollide(player, sprite_manager.mobs, True, pygame.sprite.collide_circle)
        for hit in hits:
            player.shield -= hit.radius * 2
            expl = Explosion(hit.rect.center, 'sm')
            sprite_manager.all_sprites.add(expl)
            newmob()
            if player.shield <= 0:
                death_explosion = Explosion(player.rect.center, 'player')
                sprite_manager.all_sprites.add(death_explosion)
                player.hide()
                player.lives -= 1
                player.shield = 100

        # Проверка столкновений игрока и улучшения
        hits = pygame.sprite.spritecollide(player, sprite_manager.powerups, True)
        for hit in hits:
            if hit.type == 'shield':
                player.shield += random.randrange(10, 30)
                if player.shield >= 100:
                    player.shield = 100
            if hit.type == 'gun':
                player.powerup()
                player.power_sound.play()

        # Если игрок умер, игра окончена
        if player.lives == 0 and not death_explosion.alive():
            game_over = True
            start_game = True

        # Рендеринг
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        sprite_manager.all_sprites.draw(screen)
        draw_text(screen, str(score), 18, WIDTH / 2, 10)
        draw_shield_bar(screen, 5, 5, player.shield)
        draw_lives(screen, WIDTH - 100, 5, player.lives,
                   player.player_mini_img)
        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()

    pygame.quit()