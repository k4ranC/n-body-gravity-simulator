from body import Body
import numpy as np


def create_black_hole_system():
    black_hole = Body(
        mass=50000,
        position=[0, 0],
        velocity=[0, 0],
        radius=15,
        body_type="black_hole"
    )

    bodies = [black_hole]

    for _ in range(50):
        distance = np.random.uniform(80, 180)
        angle = np.random.uniform(0, 2 * np.pi)

        x = distance * np.cos(angle)
        y = distance * np.sin(angle)

        # Tangential velocity for orbit-like movement
        speed = np.random.uniform(8, 14)
        vx = -np.sin(angle) * speed
        vy = np.cos(angle) * speed

        particle = Body(
            mass=1,
            position=[x, y],
            velocity=[vx, vy],
            radius=2,
            body_type="particle"
        )

        bodies.append(particle)

    return bodies