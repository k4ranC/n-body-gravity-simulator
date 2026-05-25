from body import Body
import numpy as np


def create_black_hole_system():
    # Same scale as solar system:
    # distance = million km
    # time = days
    # mass = kg

    black_hole = Body(
        mass=1.989e31,
        position=[0, 0],
        velocity=[0, 0],
        radius=300,
        body_type="black_hole",
        name="Black Hole"
    )

    bodies = [black_hole]

    for _ in range(40):
        # Randomly place particles in a disk around the black hole
        distance = np.random.uniform(150, 400)
        angle = np.random.uniform(0, 2 * np.pi)

        x = distance * np.cos(angle)
        y = distance * np.sin(angle)

        # Approximate circular orbital speed:
        # v = sqrt(GM/r)
        G_scaled = 4.982e-28
        speed = np.sqrt(G_scaled * black_hole.mass / distance)

        # Add randomness so particles do not form perfect circles
        speed *= np.random.uniform(0.8, 1.15)

        vx = -np.sin(angle) * speed
        vy = np.cos(angle) * speed

        particle = Body(
            mass=1e18,
            position=[x, y],
            velocity=[vx, vy],
            radius=300,
            body_type="particle",
        )

        bodies.append(particle)

    return bodies