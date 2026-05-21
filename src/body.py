import numpy as np


class Body:
    def __init__(self, mass, position, velocity, radius=4, body_type="planet"):
        self.mass = mass
        self.radius = radius
        self.body_type = body_type

        # Position and velocity are vectors
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        
        # Force accumulator
        self.force = np.zeros(2)

    def update(self, timestep):
        # a = F / m
        acceleration = self.force / self.mass

        # Update velocity
        self.velocity += acceleration * timestep

        # Update position
        self.position += self.velocity * timestep

        # Reset force after update
        self.force = np.zeros(2)