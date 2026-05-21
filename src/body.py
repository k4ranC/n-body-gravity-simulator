import numpy as np


class Body:
    def __init__(self, mass, position, velocity):
        self.mass = mass

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