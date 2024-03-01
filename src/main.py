import pygame
from Snake import Snake
from game_utils import GameUtils
from Fruit import Fruit
from pygame.math import Vector2


class Main:
    def __init__(self, width, height, cell_size, cell_number, game_font):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.cell_number = cell_number
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.snake = Snake(self.screen, self.cell_size, self.cell_number)
        self.fruit = Fruit(self.screen, self.cell_size, self.cell_number)
        self.game_font = game_font

    def update(self):
        self.snake.move_snake()
        self.check_collision()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()


    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < self.cell_number or not 0 <= self.snake.body[0].y < self.cell_size:
            GameUtils.close_game()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                GameUtils.close_game()

    def draw_grass(self):
        grass_color = (167, 209, 61)
        for row in range(self.cell_number):
            if row % 2 == 0:
                for col in range(self.cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                        pygame.draw.rect(self.screen, grass_color, grass_rect)
            else:
                for col in range(self.cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                        pygame.draw.rect(self.screen, grass_color, grass_rect)

    def draw_score(self):
        score_text = len(self.snake.body) - 3
        score_surface = self.game_font.render(str(score_text), True, (56, 74, 12))
        x_score = self.cell_size * self.cell_number - 60
        y_score = self.cell_size * self.cell_number - 40
        score_rect = score_surface.get_rect(center=(x_score, y_score))
        self.screen.blit(score_surface, score_rect)
def run():
    pygame.init()
    cell_size = 25
    cell_number = 25
    game_font = pygame.font.Font(None, 25)
    game = Main(cell_number * cell_size, cell_number * cell_size, cell_size, cell_number, game_font)
    clock = pygame.time.Clock()

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameUtils.close_game()
            if event.type == SCREEN_UPDATE:
                game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if game.snake.direction.y != 1:
                        game.snake.direction = Vector2(0, -1)
                elif event.key == pygame.K_RIGHT:
                    if game.snake.direction.x != -1:
                        game.snake.direction = Vector2(1, 0)
                elif event.key == pygame.K_DOWN:
                    if game.snake.direction.y != -1:
                        game.snake.direction = Vector2(0, 1)
                elif event.key == pygame.K_LEFT:
                    if game.snake.direction.x != 1:
                        game.snake.direction = Vector2(-1, 0)

        game.check_fail()
        game.screen.fill((175, 215, 70))
        game.draw_elements()
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    run()
