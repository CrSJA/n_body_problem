#!/usr/bin/env python3

import pygame as pg
from random import random
from constants import *
from particle import particle
from campos import*

def physics_step(group, dt, substeps=3):  # introduce una actualizacion fisica al sistema
    sub_dt = dt / substeps
    for _ in range(substeps):
        group.update(sub_dt)


def main():
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clok =  pg.time.Clock()
    dt=0

    updatable=pg.sprite.Group() 
    drawable=pg.sprite.Group()
    particles=pg.sprite.Group()

    particle.containers = (particles,updatable,drawable)
    Campo_Electrico.containers=(updatable)
 
    
    objects=[]
    
    for i in range(8):
        carga=random.randint(-1,1)
        particle(random.randint(40,1240),random.randint(40,680),20,objects,charge=random.randint(-1,1))
    
    Campo_Electrico(objects)

    particle_list = list(particles)

    while True:
        screen.fill(("black"))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            
        physics_step(updatable, dt, substeps=10) # updates an draws everiting whith substeps


        for a in drawable:
            a.draw(screen)

        for i in range(len(particle_list)):
            for j in range(i + 1, len(particle_list)):
                p = particle_list[i]
                a = particle_list[j]
                if p.is_colliding(a):
                    p.solve_collision(a)

        pg.display.flip()
        dt = (clok.tick(60))/1000

if __name__ =="__main__":
    main()
