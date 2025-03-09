import pygame
import math
import random
import numpy as np

from config import WIDTH, HEIGHT, FPS
from particle import Particle
from trail import Trail

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Slime Pathing Simulator")
clock = pygame.time.Clock()

NUM_PARTICLES = 50
MAX_TRAILS = 5000
TRAIL_FADE = 5
RANDOM_FACTOR = 1

particles = []
trails = []

# particle_positions = np.zeros((NUM_PARTICLES, 2))
# particle_velocities = np.zeros((NUM_PARTICLES, 2))
# particle_colors = np.zeros((NUM_PARTICLES, 3), dtype=np.uint8)
# trail_positions = np.zeros((MAX_TRAILS, 2))

def create_particle(x, y, color, dx, dy):
    particles.append(Particle(x, y, color, dx, dy))

running = True

def spawn_ring(center_x, center_y, num_particles, speed, color):
    angle_step = 360 / num_particles
    for i in range(num_particles):
        angle = angle_step * i
        dx = speed * math.cos(math.radians(angle))
        dy = speed * math.sin(math.radians(angle))
        create_particle(center_x, center_y, color, dx, dy)

spawn_ring(WIDTH // 2, HEIGHT // 2, NUM_PARTICLES, 5, (255, 255, 255))


while running:

    fade_surface = pygame.Surface((WIDTH, HEIGHT))
    fade_surface.set_alpha(TRAIL_FADE)
    fade_surface.fill((0, 0, 0))

    screen.blit(fade_surface, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for particle in particles:
        particle.move(particle.dx + random.randrange(-RANDOM_FACTOR, RANDOM_FACTOR), particle.dy + random.randrange(-RANDOM_FACTOR, RANDOM_FACTOR))
        particle.draw(screen)
        trails.append(Trail(particle.x, particle.y))

        front_x = particle.x + particle.dx * 3
        front_y = particle.y + particle.dy * 3

        for trail in trails:
            if math.hypot(trail.x - front_x, trail.y - front_y) < 5:
                angle_to_trail = math.atan2(trail.y - particle.y, trail.x - particle.x)
                angle_to_trail += random.uniform(-0.1, 0.1)
                particle.dx = 5 * math.cos(angle_to_trail)
                particle.dy = 5 * math.sin(angle_to_trail)
                break

        if len(trails) > MAX_TRAILS:
            trails.pop(0)

        if(particle.x <= 0 or particle.x >= WIDTH or particle.y <= 0 or particle.y >= HEIGHT):
            angle = random.uniform(0, 2 * np.pi)
            particle.dx = 5 * math.cos(angle)
            particle.dy = 5 * math.sin(angle)

    for trail in trails:
        trail.draw(screen)


    clock.tick(FPS)

    fade_surface = pygame.Surface((WIDTH, HEIGHT))
    fade_surface.set_alpha(TRAIL_FADE)
    fade_surface.fill((0, 0, 0))

    screen.blit(fade_surface, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()
