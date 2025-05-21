from circleshape import *
from constants import *
import random

class asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.time_of_existence=40
    
    def draw(self, screen):
        pygame.draw.circle(screen,"white",(self.position),self.radius,2)
    
    def update(self,dt):
        self.position +=self.velocity*dt
        self.time_of_existence-=dt
        if self.time_of_existence < 0:
            self.kill()

    def split(self):
        self.kill()
        if self.radius<= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50) # random n betuin 20 and 50

            a = asteroid(self.position.x,self.position.y,self.radius/2)
            a.velocity=(self.velocity.rotate(random_angle))*1.5

            a = asteroid(self.position.x,self.position.y,self.radius/2)
            a.velocity=(self.velocity.rotate(-random_angle))*1.5
