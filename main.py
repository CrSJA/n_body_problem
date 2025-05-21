import pygame as pg
from constants import *
from player import player
from asteroid import asteroid
from asteroidfield import AsteroidField
from shot import shoot
def main():
    
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clok =  pg.time.Clock()
    dt=0

    updatable=pg.sprite.Group() 
    drawable=pg.sprite.Group()
    asteroids=pg.sprite.Group()
    shoots=pg.sprite.Group()

    player.containers = (updatable,drawable) # adds all player instances to two groups must be before declaration of object player
    asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    shoot.containers=(updatable,drawable,shoots)

    playe=player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    assfield=AsteroidField()



    while True:
        screen.fill(("black"))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            
        
        updatable.update(dt)   # updates and draws everiting
        for a in asteroids:
            if a.is_coliding(playe):
                print("game over")
                return

        for asteroir in asteroids:
            for bullet in shoots:
                if asteroir.is_coliding(bullet):
                    asteroir.split()
                    bullet.kill()  
                    pass


        for a in drawable:
            a.draw(screen)
        
        pg.display.flip()
        dt = (clok.tick(60))/1000


if __name__ =="__main__":
    main()