import pygame
import random

from objects.base import DrawableObject
from constants import Cell, Color


class SemenObject(DrawableObject):
    all_counter = 0
    alive_counter = 0
    pygame.init()

    sound_earn_semen = pygame.mixer.Sound('sounds/waka_waka.wav')


    def __init__(self, game, field, pacman, value=1) -> None:
        super().__init__(game)
        self.field = field
        self.eaten = False
        self.value = value  # 1 - classic, 2 - energiser
        self.x = 0
        self.y = 0
        self.pacman = pacman
        self.radiusAnim = 1
        if self.value == 1:
            self.radius = Cell.CELL_SIZE // 4
        elif self.value == 2:
            self.radius = Cell.CELL_SIZE // 2
        # self.rect = pygame.rect.Rect(0, 0, 0, 0)

    def check_eaten(self):
        if not self.eaten:
            if self.x == self.pacman.x and self.y == self.pacman.y:
                self.pacman.increase_points(self.value)
                self.eaten = True
                SemenObject.alive_counter -= 1
                if not self.game.sound_channel.get_busy():
                    self.game.sound_channel.play(self.sound_earn_semen)            
                
    def move_center(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def get_position(self):
        return tuple((self.x * Cell.CELL_SIZE + Cell.CELL_SIZE // 2 + 4,
                      self.y * Cell.CELL_SIZE + Cell.CELL_SIZE // 2 + 4))
    def anim(self):
        if self.radiusAnim < 0:
            self.radius += self.radiusAnim
            self.radiusAnim *= -1
        if random.randint(0, 100) == 0:
            self.radius += self.radiusAnim
            self.radiusAnim *= -1

    def process_logic(self) -> None:
        self.check_eaten()
        self.anim()
        self.process_draw()

    def process_draw(self) -> None:
        if not self.eaten:
            pygame.draw.circle(self.game.screen, (144, 224, 239), self.get_position(), self.radius)
