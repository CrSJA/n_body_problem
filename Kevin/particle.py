from circleshape import *
from constants import *
from system import *
import pygame as pg
import random

class particle(CircleShape):
    def __init__(self, x, y, radius,system,mass=1,charge=0):
        super().__init__(x, y, radius)
        self.mass=mass
        self.charche=charge
        self.system=system
        self.system.append(self)
    
    def draw(self, screen):
        pygame.draw.circle(screen,"white",(self.position),self.radius,2)
    
    def update(self,dt):
        self.velocity +=self.acceleration*dt
        self.position +=self.velocity*dt

    def solve_force(self,another):
        pass

    def split(self):
        self.kill()
        if self.radius<= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50) # random n betuin 20 and 50

            a = asteroid(self.position.x,self.position.y,self.radius/2,self.__mass/2)
            a.velocity=(self.velocity.rotate(random_angle))*1.5

            a = asteroid(self.position.x,self.position.y,self.radius/2,self.__mass/2)
            a.velocity=(self.velocity.rotate(-random_angle))*1.5
