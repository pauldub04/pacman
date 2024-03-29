import pygame

from constants import Cell
from objects.base import DrawableObject


class FieldObject(DrawableObject):
    def __init__(self, game) -> None:
        super().__init__(game)
        self.map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
                    [1, 3, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 3, 1],
                    [1, 3, 1, 0, 0, 1, 3, 1, 0, 0, 0, 1, 3, 1, 1, 3, 1, 0, 0, 0, 1, 3, 1, 0, 0, 1, 3, 1],
                    [1, 3, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 3, 1],
                    [1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
                    [1, 3, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 3, 1],
                    [1, 3, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 3, 1],
                    [1, 3, 3, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 1],
                    [1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 6, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 3, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 3, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 3, 1, 1, 3, 1, 1, 1, 4, 4, 1, 1, 1, 3, 1, 1, 3, 1, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 0, 0, 0, 0, 0, 0, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1],
                    [2, 3, 3, 3, 3, 5, 3, 3, 3, 3, 1, 0, 0, 0, 0, 0, 0, 1, 3, 3, 3, 3, 5, 3, 3, 3, 6, 2],
                    [1, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 0, 0, 0, 0, 0, 0, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 3, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 3, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1],
                    [1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
                    [1, 3, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 3, 1],
                    [1, 3, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 3, 1],
                    [1, 3, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 3, 3, 3, 1],
                    [1, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 1],
                    [1, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 1],
                    [1, 3, 3, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 1],
                    [1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1],
                    [1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1],
                    [1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 6, 3, 3, 3, 3, 3, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        # на карте 0 - пусткая клетка, 1 - стена, 2 - телепорт (слева и вправа)
        self.color = (55, 0, 255)
        self.draw_squares = 0
        self.draw_bg = 1
        self.teleports = ((14, 0), (14, Cell.WIDTH_CNT - 1))

    def is_available_point(self, x, y):
        try:
            if self.map[y][x] != 1 and self.map[y][x] != 5:
                pass
        except IndexError:
            return False
        else:
            if self.map[y][x] != 1 and self.map[y][x] != 5:
                return True
            return False

    @staticmethod
    def get_cell_position(i, j):
        return tuple((j * Cell.CELL_SIZE, i * Cell.CELL_SIZE))
        # сначала j потом i, т.к. в двумерном массиве 1 индекс - номер ряда (y), а 2 индекс номер столбца (x)

    def get_tp_coordinates(self, i, j):  # получить координаты выхода из тп
        if (i, j) == self.teleports[0]:
            return self.teleports[1]
        else:
            return self.teleports[0]

    def process_draw(self) -> None:
        if self.draw_bg:
            bg = pygame.image.load('images/background.png')
            self.game.screen.blit(bg, (3, 3))

        if self.draw_squares:
            for i in range(len(self.map)):
                for j in range(len(self.map[i])):
                    if self.map[i][j] == 1:  # стена
                        pos = self.get_cell_position(i, j)  # координаты начала клетки
                        pygame.draw.rect(self.game.screen, self.color,
                                         (pos[0] + 7, pos[1] + 7, Cell.CELL_SIZE - 7, Cell.CELL_SIZE - 7))
                    elif self.map[i][j] == 4:
                        pos = self.get_cell_position(i, j)
                        pygame.draw.rect(self.game.screen, (255, 206, 206),
                                         (pos[0] + 7, pos[1] + 7, Cell.CELL_SIZE - 7, Cell.CELL_SIZE - 7))
                    else:
                        pass
