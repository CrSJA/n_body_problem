from circleshape import *
from constants import *
from system import *
import pygame as pg
import random


class particle(CircleShape):
    def __init__(self, x, y, radius,system,mass=1,charge=0):
        super().__init__(x, y, radius)
        self.mass=mass
        self.charge=charge
        self.system=system
        self.system.append(self)
    
    def draw(self, screen):
        pygame.draw.circle(screen,"white",(self.position),self.radius,2)
    
    def update(self,dt):
        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt
        self.acceleration = pygame.Vector2()  # Reset for next frame


    def __solve_overlap(self, another):
        delta = self.position - another.position
        distance = delta.length()

        if distance == 0:
            delta = pygame.Vector2(0.01, 0)
            distance = 0.01

        normal = delta.normalize()
        overlap = self.radius + another.radius - distance

        if overlap <= 0:
            return

        correction = normal * overlap

        total_mass = self.mass + another.mass
        self.position += correction * (another.mass / total_mass)
        another.position -= correction * (self.mass / total_mass)




    def solve_collision(self,another):



        self.__solve_overlap(another)
        
        delta = self.position - another.position
        distance = delta.length()

        if distance == 0:
            return  # Prevent division by zero

        normal = delta.normalize()
        relative_velocity = self.velocity - another.velocity

        # Only resolve if moving toward each other
        velocity_along_normal = relative_velocity.dot(normal)
        if velocity_along_normal > 0:
            return

        restitution = 0.95  # Elastic collision
        impulse_mag = -(1 + restitution) * velocity_along_normal
        impulse_mag /= (1 / self.mass + 1 / another.mass)

        impulse = impulse_mag * normal
        self.velocity += impulse / self.mass
        another.velocity -= impulse / another.mass
        pass



    def solve_force(self,another):
        pass

