import numpy as np

import body


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

                if not body_a.is_active or not body_b.is_active:
                    continue

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
        self.handle_absorption()

        for body in self.bodies:
            if body.is_active:
                body.update(timestep)

    def handle_absorption(self):
        black_holes = [body for body in self.bodies if body.body_type == "black_hole"]

        for black_hole in black_holes:
            for body in self.bodies:
                if body is black_hole or not body.is_active:
                    continue

                distance = np.linalg.norm(body.position - black_hole.position)

                if distance < black_hole.radius:
                    body.is_active = False