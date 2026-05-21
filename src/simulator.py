import numpy as np


class Simulator:
    def __init__(self, bodies, gravitational_constant=1.0):
        self.bodies = bodies
        self.G = gravitational_constant

    def calculate_gravity(self):
        for body in self.bodies:
            body.force = np.zeros(2)

        for i in range(len(self.bodies)):
            for j in range(i + 1, len(self.bodies)):
                body_a = self.bodies[i]
                body_b = self.bodies[j]

                direction = body_b.position - body_a.position
                distance = np.linalg.norm(direction)

                if distance == 0:
                    continue

                force_magnitude = self.G * body_a.mass * body_b.mass / distance**2
                force_direction = direction / distance
                force = force_magnitude * force_direction

                body_a.force += force
                body_b.force -= force

    def step(self, timestep):
        self.calculate_gravity()

        for body in self.bodies:
            body.update(timestep)