from body import Body


def create_solar_system():
    # Scale:
    # distance: 1 unit = 1 million km
    # velocity: million km per day
    # time = days

    sun = Body(
        mass=1.989e30,
        position=[0, 0],
        velocity=[0, 0],
        radius=12,
        body_type="star"
    )

    neptune = Body(
        mass=1.024e26,
        position=[4495, 0],     # 4495 million km from Sun
        velocity=[0, 0.47],    # ~5.43 km/s converted to million km/day
        radius=8,
        body_type="planet"
    )

    uranus = Body(
        mass=8.681e25,
        position=[2871, 0],     # 2871 million km from Sun
        velocity=[0, 0.59],    # ~6.81 km/s converted to million km/day
        radius=7,
        body_type="planet"
    )

    saturn = Body(
        mass=5.683e26,
        position=[1427, 0],     # 1427 million km from Sun
        velocity=[0, 0.84],    # ~9.69 km/s converted to million km/day
        radius=9,
        body_type="planet"
    )

    jupiter = Body(
        mass=1.898e27,
        position=[778.5, 0],      # 778.5 million km from Sun
        velocity=[0, 1.13],      # ~13.07 km/s converted to million km/day
        radius=10,
        body_type="planet"
    )

    mars = Body(
        mass=6.39e23,
        position=[227.9, 0],     # 227.9 million km from Sun
        velocity=[0, 2.08],     # ~24.077 km/s converted to million km/day
        radius=4,
        body_type="planet"
    )

    earth = Body(
        mass=5.972e24,
        position=[149.6, 0],     # 149.6 million km from Sun
        velocity=[0, 2.57],       # ~29.78 km/s converted to million km/day
        radius=5,
        body_type="planet"
    )

    venus = Body(
        mass=4.867e24,
        position=[108.2, 0],     # 108.2 million km from Sun
        velocity=[0, 3.02],      # ~35.02 km/s converted to million km/day
        radius=4,
        body_type="planet"
    )

    mercury = Body(
        mass=3.285e23,
        position=[57.9, 0],      # 57.9 million km from Sun
        velocity=[0, 4.09],      # ~47.87 km/s converted to million km/day
        radius=3,
        body_type="planet"
    )

    return [sun, neptune, uranus, saturn, jupiter, mars, earth, venus, mercury]