import pygame

PIXEL_SIZE = 5 

class Particle:
    def __init__(self, x, y, color, dy, dx):
        self.x = x
        self.y = y
        self.color = color
        self.dy = dy
        self.dx = dx

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, PIXEL_SIZE, PIXEL_SIZE))