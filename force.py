from circleshape import *
from constants import *
import random
import pygame as pg

class Force(pg.sprite.Sprite):
    def __init__(self, particle1, particle2):
        super().__init__(self.containers)
        self.particle1 = particle1
        self.particle2 = particle2

    def update(self,dt):
        f=self.solve_force()
        self.particle1.acceleration=1*f/self.particle1.mass
        self.particle2.acceleration=-1*f/self.particle2.mass

    def solve_force(self):
        #mus override
        pass
