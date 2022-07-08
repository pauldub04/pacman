import pygame
import math
import random
from .ghost import GhostObject
from constants import Modes, AimPoint, SpawnPoints, SpriteConstants, TimerValue


class BlueGhost(GhostObject):
    def __init__(self, game, field, coordinates, pacman, red_ghost):
        super().__init__(game, field, coordinates, pacman)
        self.img_path = "images/ghosts/blue_ghost"
        self.image = None
        self.aim_point = AimPoint.BLUE_WAITING
        self.set_img()
        self.red_ghost = red_ghost
        self.was_30_points_eaten = False

    def process_scatter_logic(self):
        if self.previous_position is None:
            ways = [(0, -1), (-1, 0), (0, 1), (1, 0)]
            possible_direction = []
            for i in range(4):
                if ways[i] == (0, 1):
                    if 12 <= self.position[0] <= 15 and self.position[1] + ways[i][1] == 12 and self.is_ghost_live():
                        continue
                    else:
                        if self.field.is_available_point(self.position[0] + ways[i][0], self.position[1] + ways[i][1]):
                            possible_direction.append(i)
                else:
                    if self.field.is_available_point(self.position[0] + ways[i][0], self.position[1] + ways[i][1]):
                        possible_direction.append(i)
            tmp_way = possible_direction[0]
            tmp_dist = int(math.hypot((self.position[0] + ways[tmp_way][0]) - self.aim_point[0],
                                      (self.position[1] + ways[tmp_way][1]) - self.aim_point[1]))
            for i in range(1, len(possible_direction)):
                new_possible_dist = int(
                    math.hypot((self.position[0] + ways[possible_direction[i]][0]) - self.aim_point[0],
                               (self.position[1] + ways[possible_direction[i]][1]) - self.aim_point[1])
                )
                if new_possible_dist < tmp_dist:
                    tmp_way = possible_direction[i]
                    tmp_dist = new_possible_dist
            self.direction = tmp_way + 1
            self.previous_position = self.position
            self.position = (self.position[0] + ways[tmp_way][0], self.position[1] + ways[tmp_way][1])
        else:
            ways = [(0, -1), (-1, 0), (0, 1), (1, 0)]
            possible_direction = []
            for i in range(4):
                if (i - 2) % 4 + 1 != self.direction:
                    if ways[i] == (0, 1):
                        if 12 <= self.position[0] <= 15 and 12 <= self.position[1] + ways[i][
                            1] == 15 and self.is_ghost_live():
                            continue
                        else:
                            if self.field.is_available_point(self.position[0] + ways[i][0],
                                                             self.position[1] + ways[i][1]):
                                possible_direction.append(i)
                    else:
                        if self.field.is_available_point(self.position[0] + ways[i][0], self.position[1] + ways[i][1]):
                            possible_direction.append(i)
            tmp_way = possible_direction[0]
            tmp_dist = int(math.hypot((self.position[0] + ways[tmp_way][0]) - self.aim_point[0],
                                      (self.position[1] + ways[tmp_way][1]) - self.aim_point[1]))
            for i in range(1, len(possible_direction)):
                new_possible_dist = int(
                    math.hypot((self.position[0] + ways[possible_direction[i]][0]) - self.aim_point[0],
                               (self.position[1] + ways[possible_direction[i]][1]) - self.aim_point[1])
                )
                if new_possible_dist < tmp_dist:
                    tmp_way = possible_direction[i]
                    tmp_dist = new_possible_dist
            self.direction = tmp_way + 1
            self.previous_position = self.position
            self.position = (self.position[0] + ways[tmp_way][0], self.position[1] + ways[tmp_way][1])
        self.set_img()

    def process_chase_logic(self):
        ways = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        point_of_pacman = None
        # 1 = up, 2 = right, 3 = down, 4 = left, 0 = nothing
        if self.pacman.direction == 0:
            point_of_pacman = (
                self.pacman.x + (self.pacman.x - self.red_ghost.position[0]),
                self.pacman.y + (self.pacman.y - self.red_ghost.position[1])
            )
        elif self.pacman.direction == 1:
            point_of_pacman = (
                (self.pacman.x - 4) + ((self.pacman.x - 4) - self.red_ghost.position[0]),
                (self.pacman.y - 4) + ((self.pacman.y - 4) - self.red_ghost.position[1])
            )
        elif self.pacman.direction == 2:
            point_of_pacman = (
                (self.pacman.x + 2) + ((self.pacman.x + 2) - self.red_ghost.position[0]),
                self.pacman.y + (self.pacman.y - self.red_ghost.position[1])
            )
        elif self.pacman.direction == 3:
            point_of_pacman = (
                self.pacman.x + (self.pacman.x - self.red_ghost.position[0]),
                (self.pacman.y + 2) + ((self.pacman.y + 2) - self.red_ghost.position[1])
            )
        elif self.pacman.direction == 4:
            point_of_pacman = (
                (self.pacman.x - 2) + ((self.pacman.x - 2) - self.red_ghost.position[0]),
                self.pacman.y + (self.pacman.y - self.red_ghost.position[1])
            )
        possible_direction = []
        for i in range(4):
            if (i - 2) % 4 + 1 != self.direction:
                if ways[i] == (0, 1):
                    if 12 <= self.position[0] <= 15 and self.position[1] + ways[i][1] == 12 and self.is_ghost_live():
                        continue
                    else:
                        if self.field.is_available_point(self.position[0] + ways[i][0], self.position[1] + ways[i][1]):
                            possible_direction.append(i)
                else:
                    if self.field.is_available_point(self.position[0] + ways[i][0], self.position[1] + ways[i][1]):
                        possible_direction.append(i)
        tmp_way = possible_direction[0]
        tmp_dist = int(math.hypot((self.position[0] + ways[tmp_way][0]) - point_of_pacman[0],
                                  (self.position[1] + ways[tmp_way][1]) - point_of_pacman[1]))
        for i in range(1, len(possible_direction)):
            new_possible_dist = int(
                math.hypot((self.position[0] + ways[possible_direction[i]][0]) - point_of_pacman[0],
                           (self.position[1] + ways[possible_direction[i]][1]) - point_of_pacman[1])
            )
            if new_possible_dist < tmp_dist:
                tmp_way = possible_direction[i]
                tmp_dist = new_possible_dist
        self.direction = tmp_way + 1
        self.previous_position = self.position
        self.position = (self.position[0] + ways[tmp_way][0], self.position[1] + ways[tmp_way][1])

        self.set_img()

    def process_frightening_logic(self):
        ways = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        possible_direction = []
        for i in range(4):
            if (i - 2) % 4 + 1 != self.direction:
                if ways[i] == (0, 1):
                    if 12 <= self.position[0] <= 15 and self.position[1] + ways[i][1] == 12:
                        continue
                    else:
                        if self.field.is_available_point(self.position[0] + ways[i][0], self.position[1] + ways[i][1]):
                            possible_direction.append(i)
                else:
                    if self.field.is_available_point(self.position[0] + ways[i][0], self.position[1] + ways[i][1]):
                        possible_direction.append(i)
        try:
            way = random.choice(possible_direction)
        except IndexError:
            self.direction = self.direction
            self.set_img()
        else:
            self.direction = way + 1
            self.position = (self.position[0] + ways[way][0], self.position[1] + ways[way][1])
            self.set_img()

    def process_logic(self):
        self.check_pacman()
        if self.is_ghost_live():
            if self.was_30_points_eaten:
                if self.mode == Modes.SCATTER:
                    if 12 <= self.position[0] <= 15 and 12 <= self.position[1] <= 15:
                        self.aim_point = AimPoint.BLUE_EXIT
                    else:
                        self.aim_point = AimPoint.BLUE
                    self.process_scatter_logic()
                elif self.mode == Modes.CHASE:
                    self.process_chase_logic()
                elif self.mode == Modes.FRIGHTENED:
                    self.process_frightening_logic()
            else:
                self.aim_point = AimPoint.BLUE_WAITING
                self.process_scatter_logic()
            if self.pacman.eaten_score >= 30 and not self.was_30_points_eaten:
                self.set_timer()
                self.was_30_points_eaten = True
                self.aim_point = AimPoint.BLUE_EXIT
                self.process_scatter_logic()
        else:
            if self.position == SpawnPoints.BLUE:
                self.is_live = True
                self.aim_point = AimPoint.BLUE_EXIT
                self.mode = Modes.SCATTER
                self.set_timer()
            else:
                self.process_scatter_logic()

    def set_img(self):
        # self.direction: 1 = up, 4 = right, 3 = down, 2 = left
        if self.is_live:
            if self.mode == Modes.FRIGHTENED:
                if self.photo == 1:
                    self.image = pygame.image.load("images/ghosts/frightend_ghost/1.png")
                    self.photo = 2
                else:
                    self.image = pygame.image.load("images/ghosts/frightend_ghost/2.png")
                    self.photo = 1
            else:
                if self.direction == 1:
                    self.image = pygame.image.load(self.img_path + '/blue_up.png')
                elif self.direction == 4:
                    self.image = pygame.image.load(self.img_path + '/blue_right.png')
                elif self.direction == 3:
                    self.image = pygame.image.load(self.img_path + '/blue_down.png')
                elif self.direction == 2:
                    self.image = pygame.image.load(self.img_path + '/blue_left.png')
        else:
            if self.position <= SpawnPoints.BLUE:
                self.image = pygame.image.load("images/ghosts/died_ghost/left.png")
            else:
                self.image = pygame.image.load("images/ghosts/died_ghost/right.png")

    def die(self):
        self.is_live = False
        self.mode = Modes.SCATTER
        self.aim_point = SpawnPoints.BLUE
        self.clock = None
        self.timer = None
        self.previous_timer_mode = None
        self.delta_time = None
        self.count_change_timer_mode = None

    def to_start_position(self):
        self.position = SpawnPoints.BLUE

