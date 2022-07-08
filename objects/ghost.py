import pygame

from objects.base import DrawableObject
from constants import Cell, Modes, TimerValue


class GhostObject(DrawableObject):
    def __init__(self, game, field, coordinates, pacman) -> None:
        super().__init__(game)
        self.field = field
        self.position = (coordinates[0], coordinates[1])
        self.previous_position = None
        self.pacman = pacman
        self.mode = Modes.SCATTER
        self.radius = Cell.CELL_SIZE // 2 + 2
        self.direction = 1  # 1 = up, 2 = right, 3 = down, 4 = left
        self.is_live = True
        self.clock = None
        self.timer = None
        self.previous_timer_mode = None
        self.delta_time = None
        self.count_change_timer_mode = None
        self.photo = 1

    def check_pacman(self):
        if self.pacman.rage:
            self.mode = Modes.FRIGHTENED
        else:
            self.mode = Modes.CHASE

    def get_direction(self):
        if self.direction == 1:
            return 'up' + " " + str(self.direction)
        elif self.direction == 4:
            return 'right' + " " + str(self.direction)
        elif self.direction == 3:
            return 'down' + " " + str(self.direction)
        elif self.direction == 2:
            return 'left' + " " + str(self.direction)
        else:
            return '0'

    def is_ghost_live(self):
        if self.is_live:
            return True
        return False

    def get_ghost_position(self):
        return tuple(
            (
                self.position[0] * Cell.CELL_SIZE + Cell.CELL_SIZE // 2 + 4,
                self.position[1] * Cell.CELL_SIZE + Cell.CELL_SIZE // 2 + 4
            )
        )
        # вычисляет координату пакмана на экране по номеру клетки, где он стоит

    def set_timer(self):
        self.clock = pygame.time.Clock()
        self.timer = TimerValue.SCATTER_FIRST_TWO_IT
        self.previous_timer_mode = None
        self.delta_time = 0
        self.count_change_timer_mode = 0

    def get_ghost_rect(self):
        return tuple(
            (
                self.position[0] * Cell.CELL_SIZE + Cell.CELL_SIZE // 2 - 6,
                self.position[1] * Cell.CELL_SIZE + Cell.CELL_SIZE // 2 - 6,
                Cell.CELL_SIZE,
                Cell.CELL_SIZE
            )
        )

    def process_event(self, event: pygame.event.Event) -> None:
        if self.timer is not None:
            self.timer -= self.delta_time
            if self.timer <= 0:
                if 0 <= self.count_change_timer_mode <= 3:
                    if self.previous_timer_mode is None:
                        self.timer = TimerValue.CHASE
                        self.mode = Modes.CHASE
                        self.previous_timer_mode = TimerValue.SCATTER_FIRST_TWO_IT
                        self.count_change_timer_mode += 1
                    elif self.previous_timer_mode == TimerValue.SCATTER_FIRST_TWO_IT:
                        self.timer = TimerValue.SCATTER_FIRST_TWO_IT
                        self.mode = Modes.SCATTER
                        self.previous_timer_mode = TimerValue.CHASE
                        self.count_change_timer_mode += 1
                    elif self.previous_timer_mode == TimerValue.CHASE:
                        self.timer = TimerValue.CHASE
                        self.mode = Modes.CHASE
                        self.previous_timer_mode = TimerValue.SCATTER_FIRST_TWO_IT
                        self.count_change_timer_mode += 1
                elif 4 <= self.count_change_timer_mode <= 6:
                    if self.previous_timer_mode == TimerValue.SCATTER_FIRST_TWO_IT:
                        self.timer = TimerValue.SCATTER_SECOND_TWO_IT
                        self.mode = Modes.SCATTER
                        self.previous_timer_mode = TimerValue.CHASE
                        self.count_change_timer_mode += 1
                    elif self.previous_timer_mode == TimerValue.CHASE:
                        self.timer = TimerValue.CHASE
                        self.mode = Modes.CHASE
                        self.previous_timer_mode = TimerValue.SCATTER_SECOND_TWO_IT
                        self.count_change_timer_mode += 1
                    elif self.previous_timer_mode == TimerValue.SCATTER_SECOND_TWO_IT:
                        self.timer = TimerValue.SCATTER_SECOND_TWO_IT
                        self.mode = Modes.SCATTER
                        self.previous_timer_mode = TimerValue.CHASE
                        self.count_change_timer_mode += 1
                else:
                    self.timer = None
                    self.mode = Modes.CHASE
                    self.count_change_timer_mode += 1
            self.delta_time = self.clock.tick(10) / 1000

    def process_draw(self) -> None:
        pass
