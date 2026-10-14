from barnes_hut import QuadTree
import numpy as np

class Simulator:
    def __init__(self, bodies, gravitational_constant=1.0):
        self.bodies = bodies
        self.G = gravitational_constant

    def calculate_gravity(self):
        for body in self.bodies:
            body.force = np.zeros(2)

        positions = [b.position for b in self.bodies if b.is_active]
        if not positions:
            return

        all_pos = np.array(positions)
        max_extent = np.max(np.abs(all_pos)) * 1.5

        tree = QuadTree(cx=0, cy=0, half_size=max_extent)
        for body in self.bodies:
            if body.is_active:
                tree.insert(body)

        for body in self.bodies:
            if body.is_active:
                body.force = tree.calculate_force(body, self.G)

    def step(self, timestep):
        self.calculate_gravity()
    
        for body in self.bodies:
            if body.is_active:
                body.update(timestep)
    
        self.calculate_gravity()
    
        for body in self.bodies:
            if body.is_active:
                body.finalize_update(timestep)
                # Deactivate any body that has gone NaN/Inf
                if not np.all(np.isfinite(body.position)):
                    body.is_active = False
    
        self.handle_absorption()

    def handle_absorption(self):
        black_holes = [body for body in self.bodies if body.body_type == "black_hole"]

        for black_hole in black_holes:
            for body in self.bodies:
                if body is black_hole or not body.is_active:
                    continue

                distance = np.linalg.norm(body.position - black_hole.position)

                if distance < black_hole.radius:
                    body.is_active = False