import pygame
from os import path

from db_manager.sqlite3_manager import SQLite3Manager

from game.sprite_manager import SpriteManager


sqlite_manager = SQLite3Manager(db_name='scores.db')
score = 0
img_dir = 'img'
snd_dir = 'snd'

WIDTH = 480
HEIGHT = 600
FPS = 60
POWERUP_TIME = 5000

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Test game!")
clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial')

# Загрузка всей игровой графики
background = pygame.image.load(path.join(img_dir, "space.png")).convert()
background_rect = background.get_rect()

# Загрузка мелодий игры
expl_sounds = []
for snd in ['expl3.wav', 'expl6.wav']:
    expl_sounds.append(pygame.mixer.Sound(path.join(snd_dir, snd)))

sprite_manager = SpriteManager()