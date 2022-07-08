import pygame


# https://www.pygame.org/docs/ref/color.html
# https://github.com/pygame/pygame/blob/master/src_py/colordict.py


class Scenes:
    MENU = 0
    MAIN = 1
    GAMEOVER = 2
    PAUSE = 3
    TABLE = 4


class Records:
    FILE = 'players_data/table_records.csv'
    COLUMNS = ['name', 'points']
    EXAMPLE = 'John, 0\n'
    MAX = 20


class Cell:
    CELL_SIZE = 23
    WIDTH_CNT = 28
    HEIGHT_CNT = 33


class AimPoint:
    RED = (22, 0)
    BLUE = (45, 45)
    ORANGE = (0, 45)
    PINK = (2, -2)
    RED_EXIT = (22, 0)
    BLUE_EXIT = (15, 11)
    ORANGE_EXIT = (0, 0)
    PINK_EXIT = (22, 0)
    BLUE_WAITING = (13, 14)


class TimerValue:
    SCATTER_FIRST_TWO_IT = 7
    SCATTER_SECOND_TWO_IT = 5
    CHASE = 20


class SpawnPoints:
    RED = (13, 11)
    RED_AFTER_DIE = (14, 13)
    BLUE = (15, 13)
    ORANGE = (12, 13)
    PINK = (13, 13)


class Modes:
    CHASE = 1
    SCATTER = 2
    FRIGHTENED = 3


class SpriteConstants:
    TRANSPARENT = pygame.color.Color(255, 0, 255)
    GHOST = (20, 20)


class Color:
    RED = pygame.color.Color('red')
    BLUE = pygame.color.Color('blue')
    GREEN = pygame.color.Color('green')
    BLACK = pygame.color.Color('black')
    WHITE = pygame.color.Color('white')
    ORANGE = pygame.color.Color('orange')
    YELLOW = pygame.color.Color('yellow')
    PINK = pygame.color.Color(255, 183, 255)
