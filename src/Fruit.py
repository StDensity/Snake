import pygame, random
from pygame.math import Vector2

class Fruit:
    def __init__(self, screen, cell_size=40, cell_number=50):
        self.screen = screen
        self.cell_size = cell_size
        self.cell_number = cell_number
        self.x = random.randint(0, self.cell_number-1)
        self.y = random.randint(0, self.cell_size-1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * self.cell_size, self.pos.y * self.cell_size, self.cell_size, self.cell_number)
        pygame.draw.rect(self.screen, (126, 166, 114), fruit_rect)