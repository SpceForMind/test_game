from game.constant import *


class Bullet(pygame.sprite.Sprite):
    bullet_img = pygame.image.load(path.join(img_dir, "laserBlue.png")).convert()
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = Bullet.bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # убить, если он заходит за верхнюю часть экрана
        if self.rect.bottom < 0:
            self.kill()