from circleshape import *
from constants import *
from vecfield import *
import random
import pygame as pg

class Tierra(Field):
    def __init__(self,objects):
        super().__init__(self.containers)
        self.objects=objects
    def solve_force(self,particle):
        g_acc=9.81
        r=pg.Vector2(0,1)
        return g_acc*particle.mass*r

class Luna(Field):
    def __init__(self,particle):
        super().__init__(self.containers)
        self.particle = particle

    def solve_force(self):
        g_acc=1.62
        r=pg.Vector2(0,1)
        return g_acc*self.particle.mass*r

class Jupiter(Field):
    def __init__(self,particle):
        super().__init__(self.containers)
        self.particle = particle

    def solve_force(self):
        g_acc=24.79
        r=pg.Vector2(0,1)
        return g_acc*self.particle.mass*r
