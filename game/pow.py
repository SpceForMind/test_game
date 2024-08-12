import random

from game.constant import *

class Pow(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.powerup_images = {}
        self.powerup_images['shield'] = pygame.image.load(path.join(img_dir, 'shield_gold.png')).convert()
        self.powerup_images['gun'] = pygame.image.load(path.join(img_dir, 'gun_baf.png')).convert()
        self.type = random.choice(['shield', 'gun'])
        self.image = self.powerup_images[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 2

    def update(self):
        self.rect.y += self.speedy
        # убить, если он сдвинется с нижней части экрана
        if self.rect.top > HEIGHT:
            self.kill()