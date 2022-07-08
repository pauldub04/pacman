import pygame
import sys
from game import Game


def main():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('Pacman')
    game = Game()
    game.main_loop()
    sys.exit(0)


if __name__ == '__main__':
    main()
