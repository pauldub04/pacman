import pygame
import pandas as pd

from objects.base import DrawableObject
from constants import Cell, Color


class PacmanObject(DrawableObject):
    direction = 0  # 1 = up, 2 = right, 3 = down, 4 = left, 0 = nothing
    points = 0
    lives = 5
    pygame.font.init()

    # Это загрузка звука
    def __init__(self, game, field) -> None:
        super().__init__(game)
        self.field = field
        self.start_pos = (13, 23)

        self.x = 13  # обращение в map через [y][x]!!
        self.y = 23
        self.radius = int(Cell.CELL_SIZE // 2 + 10)

        self.tp_exit = (0, 0)
        self.is_teleport = False

        self.next_speed = dict(x=0, y=0)
        self.speed = dict(x=0, y=0)  # скорость по x: -1 - смещение на клетку влево, 1 - вправо
        # скорость по y: -1 - смещение на клетку !вверх, 1 - !вниз

        self.points = 0
        self.rage = False
        self.rage_end = 0

        self.move_cnt = 0
        self.image = 'images/pacman/default.png'
        self.just_turned = 0
        self.just_died = False

    def process_event(self, event: pygame.event.Event) -> None:

        # простая обработка wasd
        if event.type == pygame.KEYDOWN:
            if PacmanObject.direction == 0:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.speed['y'] = -1
                    self.speed['x'] = 0
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.speed['y'] = 1
                    self.speed['x'] = 0
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.speed['x'] = -1
                    self.speed['y'] = 0
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.speed['x'] = 1
                    self.speed['y'] = 0
            else:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.next_speed['y'] = -1
                    self.next_speed['x'] = 0
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.next_speed['y'] = 1
                    self.next_speed['x'] = 0
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.next_speed['x'] = -1
                    self.next_speed['y'] = 0
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.next_speed['x'] = 1
                    self.next_speed['y'] = 0

            # print('speed', self.speed)
            # print('direction', PacmanObject.direction)

    @staticmethod
    def update_direction(speed):
        if speed['y'] == -1 and speed['x'] == 0:
            PacmanObject.direction = 1
        if speed['y'] == 1 and speed['x'] == 0:
            PacmanObject.direction = 3
        if speed['y'] == 0 and speed['x'] == -1:
            PacmanObject.direction = 4
        if speed['y'] == 0 and speed['x'] == 1:
            PacmanObject.direction = 2

    @staticmethod
    def get_direction():
        if PacmanObject.direction == 1:
            return 'up' + " " + str(PacmanObject.direction)
        elif PacmanObject.direction == 2:
            return 'right' + " " + str(PacmanObject.direction)
        elif PacmanObject.direction == 3:
            return 'down' + " " + str(PacmanObject.direction)
        elif PacmanObject.direction == 4:
            return 'left' + " " + str(PacmanObject.direction)
        else:
            return '0'

    def process_logic(self):
        self.move_cnt += 1

        if self.rage:
            if pygame.time.get_ticks() >= self.rage_end:
                self.rage = False
                self.rage_end = 0

        # перемещение
        if self.next_speed['x'] != 0 or self.next_speed['y'] != 0:
            map_sizeY = len(self.field.map)
            map_sizeX = len(self.field.map[0])

            probably_next_cell_y = (self.y + self.next_speed['y'] + map_sizeY) % map_sizeY
            probably_next_cell_x = (self.x + self.next_speed['x'] + map_sizeX) % map_sizeX
            probably_next_cell = self.field.map[probably_next_cell_y][probably_next_cell_x]

            if probably_next_cell in (0, 3, 5, 6):  # empty
                self.speed['y'] = self.next_speed['y']
                self.speed['x'] = self.next_speed['x']
                self.next_speed['y'] = 0
                self.next_speed['x'] = 0
                self.y += self.speed['y']
                self.x += self.speed['x']

                self.update_direction(self.speed)
                self.just_turned = 1
                return

        next_cell = self.field.map[self.y + self.speed['y']][self.x + self.speed['x']]  # next cell to go
        if next_cell in (0, 3, 5, 6):  # empty
            self.y += self.speed['y']
            self.x += self.speed['x']
            self.update_direction(self.speed)
        elif next_cell == 2:  # teleport
            self.y += self.speed['y']
            self.x += self.speed['x']
            self.is_teleport = True
            self.tp_exit = self.field.get_tp_coordinates(self.y, self.x)
        elif next_cell == 1:  # wall
            self.speed['x'] = 0
            self.speed['y'] = 0
            self.next_speed['y'] = 0
            self.next_speed['x'] = 0
            PacmanObject.direction = 0
            # print('direction', PacmanObject.direction)
        if self.just_turned == 1:
            self.just_turned = 2
        else:
            self.just_turned = 0

    def increase_points(self, val=1):
        if val == 2:
            self.rage = True  # возможно надо сделать где-то таймер, который выключает
            self.rage_end = pygame.time.get_ticks() + 10 * 1000  # 10 секунд    
        self.points += val
        self.game.total_points += val
        # self.game.total_points = self.points
        # Тут проигрывается этот звук

    def die(self):
        if self.lives > 1:
            self.lives -= 1
            self.x, self.y = self.start_pos

            self.speed = dict(x=0, y=0)
            self.next_speed = dict(x=0, y=0)

            self.move_cnt = 0
            self.image = 'images/pacman/default.png'
            self.just_died = False

            return 1
        else:
            return 0

    def get_rect(self):
        return pygame.Rect(
            self.x * Cell.CELL_SIZE - 6,
            self.y * Cell.CELL_SIZE - 6,
            self.radius*2,
            self.radius*2,
        )

    def set_img(self):
        if self.just_died:
            self.image = 'images/pacman/dead.png'
            return

        if PacmanObject.direction == 1:
            folder = 'up'
        elif PacmanObject.direction == 2:
            folder = 'right'
        elif PacmanObject.direction == 3:
            folder = 'down'
        elif PacmanObject.direction == 4:
            folder = 'left'
        else:
            folder = 0

        pic_choice = 0
        if self.move_cnt % 3 == 0:
            pic_choice = 0
        elif self.move_cnt % 3 == 1:
            pic_choice = 1
        elif self.move_cnt % 3 == 2:
            pic_choice = 2

        if pic_choice == 0 or folder == 0 \
            or self.just_turned in (1, 2) \
            or (self.x, self.y) == self.start_pos:
            self.image = 'images/pacman/default.png'
        else:
            self.image = f'images/pacman/{folder}/position{pic_choice}.png'

    def draw_pacman(self):
        self.set_img()
        image = pygame.image.load(self.image)
        # pygame.draw.rect(self.game.screen, Color.GREEN, self.get_rect())
        self.game.screen.blit(image, self.get_rect())

    def process_draw(self) -> None:
        self.draw_pacman()

        self.game.screen.blit(
            pygame.font.Font('fonts/19190.ttf', 70).render(str(self.game.total_points) + ' ', True, (255, 255, 255)),
            (10, self.game.HEIGHT - 80))
        self.game.screen.blit(
            pygame.font.Font('fonts/19190.ttf', 70).render('HP ' + str(self.lives) + ' ', True, (0, 255, 0)),
            (150, self.game.HEIGHT - 80))

        if self.is_teleport:
            self.draw_pacman()

            self.x = self.tp_exit[1]
            self.y = self.tp_exit[0]
            self.is_teleport = False
            self.tp_exit = (0, 0)
