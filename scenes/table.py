from constants import Color, Scenes, Records
from objects import ButtonObject, TextObject
from scenes import BaseScene
from pandas import read_csv, DataFrame, Index


class TableScene(BaseScene):
    def create_objects(self) -> None:
        self.table: DataFrame = self.game.records
        self.button_back = ButtonObject(
            self.game,
            self.game.WIDTH // 2 - 300, self.game.HEIGHT // 2 - 20 + 350, 200, 50,
            Color.RED, self.back, 'В меню'
        )
        self.objects: list = self.table_generator()
        self.objects.append(self.button_back)

    def table_generator(self) -> list:
        array: list = [
            TextObject(
                self.game,
                text=Records.COLUMNS[0].capitalize(),
                x=self.game.WIDTH // 2 - 200,
                y=50
            ),
            TextObject(
                self.game,
                text=Records.COLUMNS[1].capitalize(),
                x=self.game.WIDTH // 2 + 200,
                y=50
            )]
        for row in list(self.table.values):
            for element in range(len(row)):
                array.append(
                    TextObject(
                        self.game,
                        is_bold=False,
                        text=str(row[element]),
                        x=self.game.WIDTH // 2 - 200 + (400 * (element % 2)),
                        y=array[-1].rect.y + 40 - (40 * (element % 2))
                    )
                )
        return array

    def back(self) -> None:
        self.game.set_scene(Scenes.MENU)
