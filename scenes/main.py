from datetime import datetime

import pygame

from constants import SpawnPoints, Scenes, Records
from objects import FieldObject, PacmanObject, RedGhost, BlueGhost, OrangeGhost, PinkGhost
from objects.semen import SemenObject
from scenes import BaseScene


class MainScene(BaseScene):
    death_sound = pygame.mixer.Sound('sounds/pacmandies.wav')
    eat_ghost_sound = pygame.mixer.Sound('sounds/eating_ghost.wav')

    def __init__(self, game):
        super().__init__(game)

    def create_objects(self) -> None:
        self.field = FieldObject(self.game)
        self.pacman = PacmanObject(self.game, self.field)
        self.pacman.direction = 0
        self.pacman.lives = 5
        self.ghosts = [
            RedGhost(self.game, self.field, SpawnPoints.RED, self.pacman),
            OrangeGhost(self.game, self.field, SpawnPoints.ORANGE, self.pacman),
            PinkGhost(self.game, self.field, SpawnPoints.PINK, self.pacman)
        ]
        self.ghosts.append(BlueGhost(self.game, self.field, SpawnPoints.BLUE, self.pacman, self.ghosts[0]))

        self.objects.clear()
        self.objects.append(self.field)
        self.objects.append(self.pacman)

        self.total_points = 0
        for m in self.field.map:
            self.total_points += m.count(3) + m.count(6) + m.count(5)

        pygame.font.init()
        pygame.event.set_blocked(pygame.MOUSEMOTION)

        for i in range(len(self.field.map)):  # semens
            for j in range(len(self.field.map[i])):
                if not self.field.map[i][j] in (3, 5, 6):
                    continue
                tmp = None
                if self.field.map[i][j] == 3 or self.field.map[i][j] == 5:
                    tmp = SemenObject(self.game, self.field, self.pacman, 1)
                elif self.field.map[i][j] == 6:
                    tmp = SemenObject(self.game, self.field, self.pacman, 2)
                tmp.move_center(j, i)
                self.objects.append(tmp)
                SemenObject.all_counter += 1

        for ghost in self.ghosts:
            self.objects.append(ghost)
            if type(self.objects[-1]) != BlueGhost:
                self.objects[-1].set_timer()

    def process_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game.set_scene(self.game.Scenes.PAUSE)
        for item in self.objects:
            item.process_event(event)

    def end_game(self):
        pygame.time.wait(500)
        now = datetime.now()
        current_time = now.strftime("%b %d - %H:%M")
        with open(Records.FILE, 'a') as file:
            file.write(f'{current_time}, {self.pacman.total_score}\n')
        self.game.update_records()
        self.game.set_scene(Scenes.GAMEOVER)

    def check_collision_classic(self, obj):
        return ((self.pacman.x == obj.position[0] and self.pacman.y == obj.position[1])
                or (self.pacman.x == obj.position[0] and self.pacman.y - 1 == obj.position[1]
                    and PacmanObject.direction == 1 and obj.direction == 3)
                or (self.pacman.x == obj.position[0] and self.pacman.y + 1 == obj.position[1]
                    and PacmanObject.direction == 3 and obj.direction == 1)
                or (self.pacman.y == obj.position[1] and self.pacman.x + 1 == obj.position[0]
                    and PacmanObject.direction == 2 and obj.direction == 2)
                or (self.pacman.y == obj.position[1] and self.pacman.x - 1 == obj.position[0]
                    and PacmanObject.direction == 4 and obj.direction == 4)) and obj.is_ghost_live()

    def check_collision_image(self, obj):
        return self.pacman.get_rect().colliderect(obj.get_ghost_rect())

    def check_death(self):
        if self.pacman.just_died:
            self.game.sound_channel.play(self.death_sound)

            pygame.time.wait(1800)
            for ghost in self.ghosts:
                ghost.to_start_position()

            res = self.pacman.die()
            if res == 0:
                pygame.time.wait(300)
                self.game.death_game_over = True
                self.end_game()

    def check_game_over(self):
        if self.pacman.eaten_score >= self.total_points:  # обработка конца игры
            self.end_game()

    def check_pacman_on_ghost(self):
        for obj in self.objects:
            if type(obj) in (RedGhost, BlueGhost, OrangeGhost, PinkGhost):
                if self.check_collision_classic(obj) or self.check_collision_image(obj):
                    if not obj.is_live:
                        continue
                    # print(f'pacman and {obj} are on 1 cell')
                    # print(str(self.pacman.points))
                    if self.pacman.rage:
                        if not self.game.is_easter_egg():
                            self.game.sound_channel.play(self.eat_ghost_sound)

                        obj.die()
                        self.pacman.increase_total_score(20)
                    else:
                        self.pacman.just_died = True
                        break

    def additional_logic(self) -> None:
        self.check_game_over()
        self.check_death()
        self.check_pacman_on_ghost()

        # print('pacman', self.pacman.get_direction())
        # print('ghost', self.ghosts[0].get_direction())
        # print()
