from circleshape import *
from constants import *
from force import *
import random
import pygame as pg

class Gravedad(Force):
    def __init__(self, particle1, particle2):
        super().__init__(self.containers)
        self.particle1 = particle1
        self.particle2 = particle2

    def update(self,dt):
        f=self.solve_force()
        self.particle1.acceleration=1*f/self.particle1.mass
        self.particle2.acceleration=-1*f/self.particle2.mass

    def solve_force(self):
        r=self.particle2.position-self.particle1.position
        return (6*self.particle1.mass*self.particle2.mass/(r.length()**3))*r

