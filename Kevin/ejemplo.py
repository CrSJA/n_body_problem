#!/usr/bin/env python3

import pygame as pg
from random import random
from constants import *
from particle import particle
from system import System
from gravedad import Gravedad
from gravedad_planeta import Tierra
from campo_gravedad import*
from campo_electrico import*
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
    Campo_Electrico.containers=(updatable)
    Campo_Gravedad.containers=(updatable)
    #playe=player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    objects=[]
   
    P1=particle(500,350,20,objects,charge=1)
    P2=particle(700,350,20,objects, charge=-1)
    
    Campo_Electrico(objects)

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
