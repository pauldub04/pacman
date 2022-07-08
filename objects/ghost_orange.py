import pygame
import math
import random
from .ghost import GhostObject
from constants import Modes, AimPoint, SpawnPoints, TimerValue, SpriteConstants


class OrangeGhost(GhostObject):
    def __init__(self, game, field, coordinates, pacman):
        super().__init__(game, field, coordinates, pacman)
        self.img_path = "images/ghosts/orange_ghost"
        self.image = None
        self.aim_point = AimPoint.ORANGE_EXIT
        self.set_img()

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
                        if 12 <= self.position[0] <= 15 and self.position[1] + ways[i][
                            1] == 12 and self.is_ghost_live():
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
        dist_to_pacman = int(math.hypot(self.position[0] - self.pacman.x, self.position[1] - self.pacman.y))
        aim_point = None
        if dist_to_pacman >= 8:
            aim_point = (self.pacman.x, self.pacman.y)
        elif dist_to_pacman < 8:
            aim_point = AimPoint.ORANGE
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
            tmp_way = possible_direction[0]
        except IndexError:
            self.direction = self.direction
            self.set_img()
        else:
            tmp_dist = int(math.hypot((self.position[0] + ways[tmp_way][0]) - aim_point[0],
                                      (self.position[1] + ways[tmp_way][1]) - aim_point[0]))
            for i in range(1, len(possible_direction)):
                new_possible_dist = int(
                    math.hypot((self.position[0] + ways[possible_direction[i]][0]) - aim_point[0],
                               (self.position[1] + ways[possible_direction[i]][1]) - aim_point[0])
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
            if self.mode == Modes.SCATTER:
                if 12 <= self.position[0] <= 15 and 12 <= self.position[1] <= 15:
                    self.aim_point = AimPoint.ORANGE_EXIT
                else:
                    self.aim_point = AimPoint.ORANGE
                self.process_scatter_logic()
            elif self.mode == Modes.CHASE:
                self.process_chase_logic()
            elif self.mode == Modes.FRIGHTENED:
                self.process_frightening_logic()
        else:
            if self.position == SpawnPoints.ORANGE:
                self.is_live = True
                self.aim_point = AimPoint.ORANGE_EXIT
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
                    self.image = pygame.image.load(self.img_path + '/orange_up.png')
                elif self.direction == 4:
                    self.image = pygame.image.load(self.img_path + '/orange_right.png')
                elif self.direction == 3:
                    self.image = pygame.image.load(self.img_path + '/orange_down.png')
                elif self.direction == 2:
                    self.image = pygame.image.load(self.img_path + '/orange_left.png')
        else:
            if self.position <= SpawnPoints.RED_AFTER_DIE:
                self.image = pygame.image.load("images/ghosts/died_ghost/left.png")
            else:
                self.image = pygame.image.load("images/ghosts/died_ghost/right.png")

    def die(self):
        self.is_live = False
        self.mode = Modes.SCATTER
        self.aim_point = SpawnPoints.ORANGE
        self.clock = None
        self.timer = None
        self.previous_timer_mode = None
        self.delta_time = None
        self.count_change_timer_mode = None

    def to_start_position(self):
        self.position = SpawnPoints.ORANGE

    def process_draw(self) -> None:
        self.game.screen.blit(pygame.transform.scale(self.image, SpriteConstants.GHOST), self.get_ghost_rect())
