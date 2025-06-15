from circleshape import *
from constants import *
from vecfield import *
import random
import pygame as pg

class Magnet_in(Field):
    def __init__(self,objects):
        super().__init__(self.containers)
        self.objects=objects

    def campo(self,test):
        magnitud=1
        pcruz=magnitud*pg.Vector2(test.velocity.y,-test.velocity.x)
        return pcruz

    def solve_force(self,particle):
        return self.campo(particle)*particle.charge


