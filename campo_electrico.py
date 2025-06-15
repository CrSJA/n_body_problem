from circleshape import *
from constants import *
from vecfield import *
import random
import pygame as pg

class Campo_Electrico(Field):
    def __init__(self,objects):
        super().__init__(self.containers)
        self.objects=objects

    def campo(self,test):
        K=900000
        suma=pg.Vector2(0,0)
        for particle in self.objects:
            r=test.position-particle.position
            if r.length()==0 or particle == test:
                continue
            else:
                r_length=max(r.length(),0.001)
                suma+=(K*particle.charge/(r_length**3))*r
        return suma

    def solve_force(self,particle):
        return self.campo(particle)*particle.charge


