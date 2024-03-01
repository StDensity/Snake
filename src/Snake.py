import sys
from pygame.math import Vector2
import pygame


class Snake:
    def __init__(self, screen, cell_size, cell_number):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.cell_size = cell_size
        self.cell_number = cell_number
        self.screen = screen
        self.direction = Vector2(1, 0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            x_pos = block.x * self.cell_size
            y_pos = block.y * self.cell_number
            block_rect = pygame.Rect(x_pos, y_pos, self.cell_size, self.cell_number)
            pygame.draw.rect(self.screen, (183, 111, 122), block_rect)

    def move_snake(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True