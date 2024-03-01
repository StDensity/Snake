import sys
import pygame


class GameUtils:
    @staticmethod
    def close_game():
        pygame.quit()
        sys.exit()
