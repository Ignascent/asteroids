import random
from constants import *
from circleshape import *
from logger import log_event 

class Asteroid(CircleShape):
    #containers = ()

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
       pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        split_angle  = random.uniform(20, 50)
        new1_velocity = self.velocity.rotate(split_angle) * 1.2
        new2_velocity = self.velocity.rotate(-split_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = new1_velocity
        new_asteroid2.velocity = new2_velocity



