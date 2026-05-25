import numpy as np

# Simulator class to manage the physics of the n-body simulation
class Simulator:
    def __init__(self, bodies, gravitational_constant=1.0):
        self.bodies = bodies
        self.G = gravitational_constant

    # Calculate gravitational forces between all pairs of bodies and update their force accumulators
    def calculate_gravity(self):
        for body in self.bodies:
            body.force = np.zeros(2)

        # Calculate forces between each pair of bodies
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

    # Perform a single simulation step using leapfrog integration
    def step(self, timestep):
        self.calculate_gravity()

        for body in self.bodies:
            if body.is_active:
                body.update(timestep)

        self.calculate_gravity()

        for body in self.bodies:
            if body.is_active:
                body.finalize_update(timestep)

        self.handle_absorption()

    # Handle absorption of bodies by black holes
    def handle_absorption(self):
        black_holes = [body for body in self.bodies if body.body_type == "black_hole"]

        for black_hole in black_holes:
            for body in self.bodies:
                if body is black_hole or not body.is_active:
                    continue

                distance = np.linalg.norm(body.position - black_hole.position)

                if distance < black_hole.radius:
                    body.is_active = False