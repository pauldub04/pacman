from constants import Color, Scenes
from objects import ButtonObject
from scenes import BaseScene


class MenuScene(BaseScene):
    def create_objects(self) -> None:
        self.button_start = ButtonObject(
            self.game,
            self.game.WIDTH // 2 - 100, self.game.HEIGHT // 2 - 20 - 50, 200, 50,
            Color.RED, self.start_game, "Запуск игры"
        )
        self.button_records = ButtonObject(
            self.game,
            self.game.WIDTH // 2 - 100, self.game.HEIGHT // 2 - 10, 200, 50,
            Color.RED, self.show_table, 'Рекорды'
        )
        self.button_exit = ButtonObject(
            self.game,
            self.game.WIDTH // 2 - 100, self.game.HEIGHT // 2 + 50, 200, 50,
            Color.RED, self.game.exit_game, 'Выход'
        )
        self.objects = [self.button_start, self.button_records, self.button_exit]

    def start_game(self) -> None:
        for scene in self.game.scenes:
            scene.create_objects()
        self.game.set_scene(Scenes.MAIN)

    def show_table(self) -> None:
        self.game.update_records()
        self.game.scenes[Scenes.TABLE].create_objects()
        self.game.set_scene(Scenes.TABLE)

    def on_window_resize(self) -> None:
        self.button_start.move(self.game.WIDTH // 2 - 100, self.game.HEIGHT // 2 - 20 - 50)
        self.button_records.move(self.game.WIDTH // 2 - 100, self.game.HEIGHT // 2 - 10)
        self.button_exit.move(self.game.WIDTH // 2 - 100, self.game.HEIGHT // 2 + 25)
