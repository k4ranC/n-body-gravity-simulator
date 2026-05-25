import numpy as np


class Body:
    def __init__(self, mass, position, velocity, radius=4, body_type="planet", name="Body"):
        self.mass = mass
        self.radius = radius
        self.body_type = body_type
        self.name = name
        self.trail = []
        self.is_active = True

        # Position and velocity are vectors
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        
        # Force accumulator
        self.force = np.zeros(2)


    # Leapfrog integration step
    def update(self, timestep):
        # First half-step velocity update
        acceleration = self.force / self.mass
        self.velocity += 0.5 * acceleration * timestep

        # Full position update
        self.position += self.velocity * timestep

    def finalize_update(self, timestep):
        # Second half-step velocity update
        acceleration = self.force / self.mass
        self.velocity += 0.5 * acceleration * timestep

        # Reset force after full update
        self.force = np.zeros(2)