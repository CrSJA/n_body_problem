import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0,0)
        self.acceleration= pygame.Vector2(0,0)
        self.radius = radius
        

    def is_colliding(self,another):
        distance = self.position.distance_to(another.position)
        if self.radius + another.radius >= distance:
            return True
        else:
            return False
    
    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
