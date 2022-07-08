from datetime import datetime

from constants import Color, Scenes
from objects import TextObject
from scenes import BaseScene
from random import choice

class FinalScene(BaseScene):
    TEXT_FMT = 'Игра Окончена ({})'
    seconds_to_end = 15
    TEXT_DEATH = 'Молодец'
    def __init__(self, game) -> None:
        self.last_seconds_passed = 0
        super().__init__(game)
        self.update_start_time()


    def on_activate(self) -> None:
        self.update_start_time()

    def update_start_time(self) -> None:
        self.time_start = datetime.now()

    def get_gameover_text_formatted(self) -> str:
        return self.TEXT_FMT.format(self.seconds_to_end - self.last_seconds_passed)

    def create_objects(self) -> None:
        if self.game.death_game_over == True:

            self.TEXT_DEATH = choice(['Вас убили', 'Вас съели', 'Вы проиграли'])  

        self.text_death_or_win = TextObject(self.game, text=self.TEXT_DEATH, color=Color.RED,
                 x=self.game.WIDTH // 2, y=self.game.HEIGHT // 2)

        self.objects.append(self.text_death_or_win)
    def additional_logic(self) -> None:
        time_current = datetime.now()
        seconds_passed = (time_current - self.time_start).seconds
        if self.last_seconds_passed != seconds_passed:
            self.last_seconds_passed = seconds_passed
            self.objects[0].update_text(self.get_gameover_text_formatted())
        if seconds_passed >= self.seconds_to_end:
            self.game.set_scene(Scenes.MENU)

    def on_window_resize(self) -> None:
        self.text.move_center(x=self.game.WIDTH // 2, y=self.game.HEIGHT // 2)
