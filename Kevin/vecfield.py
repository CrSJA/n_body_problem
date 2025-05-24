from circleshape import *
from constants import *
import random
import pygame as pg

class Field(pg.sprite.Sprite):
    def __init__(self,objects):
        super().__init__(self.containers)
        self.objects = objects

    def update(self,dt):
        for particle in self.objects:
            f=self.solve_force(particle)
            particle.acceleration=f/particle.mass

    def solve_force(self):
        #mus override
        pass
