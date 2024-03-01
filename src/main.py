import pygame
from Snake import Snake
from game_utils import GameUtils
from Fruit import Fruit


class Game:
    def __init__(self, width=400, height=500):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))


def main():
    pygame.init()
    cell_size = 35
    cell_number = 25
    game = Game(cell_number * cell_size, cell_number * cell_size)
    clock = pygame.time.Clock()
    fruit = Fruit(game.screen, cell_size, cell_number)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameUtils.close_game()

        game.screen.fill((175, 215, 70))
        fruit.draw_fruit()
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
