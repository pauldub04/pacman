import pygame
import os.path
from constants import Color, Cell, Scenes, Records
from scenes import MainScene, MenuScene, FinalScene, PauseScene, TableScene
from scenes.overlay import OverlayScene
from pandas import read_csv, DataFrame, Index


def get_records() -> str:
    if not os.path.isfile(Records.FILE):
        with open(Records.FILE, 'a') as file:
            file.write(Records.EXAMPLE)
    table_of_scores = read_csv(Records.FILE, delimiter=',', names=Records.COLUMNS)
    table_of_scores.sort_values(by=[Records.COLUMNS[1]], inplace=True, ascending=False)
    return table_of_scores


class Game:
    pygame.font.init()
    SIZE = WIDTH, HEIGHT = Cell.WIDTH_CNT * Cell.CELL_SIZE + 5, (Cell.HEIGHT_CNT + 2) * Cell.CELL_SIZE
    current_scene_index = Scenes.MENU
    USE_FPS_OVERLAY = False
    sound_channel = pygame.mixer.Channel(1)
    death_game_over = False

    try:
        metallica = pygame.mixer.Sound('../rock_easter_egg/Metallica_-_Fuel_47955068.wav')
        sex_pistols = pygame.mixer.Sound('sounds/rock_easter_egg/Sex_Pistols_-_Anarchy_In_The_UK_47993089.wav')
        ramones = pygame.mixer.Sound('../rock_easter_egg/Ramones_-_Blitzkrieg_Bop_48025340.wav')
        rammstein = pygame.mixer.Sound('../rock_easter_egg/Rammstein_-_Links_2_3_4_57658981.wav')
        kino = pygame.mixer.Sound('../rock_easter_egg/Kino_-_KHochu_peremen_55527255.wav')
    except:
        pass

    def __init__(self) -> None:
        self.records = get_records()
        self.high_score = max(self.records[Records.COLUMNS[1]])
        self.screen = pygame.display.set_mode(self.SIZE)
        self.scenes = [MenuScene(self), MainScene(self), FinalScene(self), PauseScene(self), TableScene(self)]
        if self.USE_FPS_OVERLAY:
            self.overlay = OverlayScene(self)
        self.game_over = False

    @staticmethod
    def exit_button_pressed(event: pygame.event.Event) -> bool:
        return event.type == pygame.QUIT

    '''
    def is_easter_egg(self):
        return self.name.lower() == 'james hetfield' or self.ID.lower() == 'till lindemann' or self.ID.lower() == 'joey ramone' or self.ID.lower() == 'виктор цой' or self.ID.lower() == 'sid vicious' or self.ID.lower() == 'punk'

    def play_easter_egg(self):
        if self.name.lower() == 'james hetfield':
            self.sound_channel.play(self.metallica)
        elif self.name.lower() == 'till lindemann':
            self.sound_channel.play(self.rammstein)
        elif self.name.lower() == 'sid vicious' or self.ID.lower() == 'punk':
            self.sound_channel.play(self.sex_pistols)
        elif self.name.lower() == 'joey ramone':
            self.sound_channel.play(self.ramones)
        elif self.name.lower() == 'виктор цой':
            self.sound_channel.play(self.kino)
    '''

    @staticmethod
    def exit_hotkey_pressed(event: pygame.event.Event) -> bool:
        return event.type == pygame.KEYDOWN and event.mod & pygame.KMOD_CTRL and event.key == pygame.K_q

    def process_exit_events(self, event: pygame.event.Event) -> None:
        if Game.exit_button_pressed(event) or Game.exit_hotkey_pressed(event):
            self.exit_game()

    def resize_scenes(self) -> None:
        for scene in self.scenes:
            scene.on_window_resize()
        if self.USE_FPS_OVERLAY:
            self.overlay.on_window_resize()

    def process_resize_event(self, event: pygame.event.Event) -> None:
        if event.type != pygame.VIDEORESIZE:
            return
        self.SIZE = self.WIDTH, self.HEIGHT = event.w, event.h
        self.screen = pygame.display.set_mode(self.SIZE, pygame.RESIZABLE)
        self.resize_scenes()

    def process_all_events(self) -> None:
        for event in pygame.event.get():
            self.process_exit_events(event)
            # self.process_resize_event(event)
            self.scenes[self.current_scene_index].process_event(event)
            if self.USE_FPS_OVERLAY:
                self.overlay.process_event(event)

    def process_all_logic(self) -> None:
        self.scenes[self.current_scene_index].process_logic()
        if self.USE_FPS_OVERLAY:
            self.overlay.process_logic()

    def process_all_draw(self) -> None:
        self.screen.fill(Color.BLACK)
        self.scenes[self.current_scene_index].process_draw()
        self.screen.blit(pygame.font.Font('fonts/19190.ttf', 70).render(f'H.S. {self.high_score}', True, (255, 0, 0)),
                         (self.WIDTH // 2 + 50, self.HEIGHT - 80))
        if self.USE_FPS_OVERLAY:
            self.overlay.process_draw()

        pygame.display.flip()

    def main_loop(self) -> None:
        '''
        if self.is_easter_egg():
            self.play_easter_egg()
        '''
        while not self.game_over:
            self.process_all_events()
            self.process_all_logic()
            self.process_all_draw()
            pygame.time.wait(130)
            # pygame.time.wait(1000)

    def set_scene(self, index: int, resume: bool = False) -> None:
        if not resume:
            self.scenes[self.current_scene_index].on_deactivate()
        self.current_scene_index = index
        if not resume:
            self.scenes[self.current_scene_index].on_activate()

    def exit_game(self) -> None:
        self.game_over = True

    def is_easter_egg(self):
        pass
