from circleshape import *
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(
            screen, 
            "white",
            self.position,
            self.radius,
            LINE_WIDTH
            )
        return

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            rand_angle = random.uniform(20,50)
            vec_1 = self.velocity.rotate(rand_angle)
            vec_2 = self.velocity.rotate(-rand_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid_2 = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid_1.velocity = vec_1 * 1.2
            asteroid_2.velocity = vec_2 * 1.2

            