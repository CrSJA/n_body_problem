#!/usr/bin/env python3

import pygame as pg
from random import random
from constants import *
from particle import particle
from system import System
from gravedad import Gravedad
from gravedad_planeta import Tierra
from campo_gravedad import*
def main():
    
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clok =  pg.time.Clock()
    dt=0

    updatable=pg.sprite.Group() 
    drawable=pg.sprite.Group()
    particles=pg.sprite.Group()

    particle.containers = (particles,updatable,drawable)
    System.containers = (updatable)
    #Gravedad.containers = (updatable)
    Tierra.containers=(updatable)
    Campo_Gravedad.containers=(updatable)
    #playe=player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    objects=[]
   
    sol=particle(600,350,100,objects, mass=10000000)
    
    for i in range(8): 
        p=particle(1200*random.random(),700*random.random(),20,objects, mass=1000)
        p.velocity=100*pg.Vector2(random.random(),random.random())
    #Tierra(objects)
    Campo_Gravedad(objects)

    while True:
        screen.fill(("black"))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            
        
        updatable.update(dt)   # updates and draws everiting
       
        '''
        for a in asteroids:
            if a.is_coliding(playe):
                print("game over")
                return
        '''

        '''
        for asteroir in asteroids:
            for bullet in shoots:
                if asteroir.is_coliding(bullet):
                    asteroir.split()
                    bullet.kill()  
                    pass
        '''
        
        for a in drawable:
            a.draw(screen)
        
        pg.display.flip()
        dt = (clok.tick(60))/1000


if __name__ =="__main__":
    main()
