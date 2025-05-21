from circleshape import CircleShape
from constants import *
import pygame


class shoot(CircleShape):
    def __init__(self, x,y):
        super().__init__(x, y, radius=SHOT_RADIUS)
        self.time_of_existence=10

    def draw(self, screen):
        pygame.draw.circle(screen,"white",(self.position),self.radius,2)
    
    def update(self,dt):
        self.position +=self.velocity*dt
        self.time_of_existence-=dt
        if self.time_of_existence<0:
            self.kill()