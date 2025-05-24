from circleshape import *
from constants import *
from vecfield import *
import random
import pygame as pg

class Campo_Gravedad(Field):
    def __init__(self,objects):
        super().__init__(self.containers)
        self.objects=objects
    def campo(self,test):
        G=6.67*10**(-2)
        suma=pg.Vector2(0,0)
        for particle in self.objects:
            r=particle.position-test.position
            if r.length()==0:
                continue
            else:
                suma+=(G*particle.mass/(r.length()**3))*r
        return suma
    def solve_force(self,particle):
        return self.campo(particle)*particle.mass


