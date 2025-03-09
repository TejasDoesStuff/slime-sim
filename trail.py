import pygame

class Trail:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (int(self.x), int(self.y)), 1)
