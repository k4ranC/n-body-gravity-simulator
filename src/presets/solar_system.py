from body import Body


from body import Body


def create_solar_system():
    # Scale:
    # distance: 1 unit = 1 million km
    # velocity: million km per day

    sun = Body(
        mass=1.989e30,
        position=[0, 0],
        velocity=[0, 0],
        radius=12,
        body_type="star"
    )

    earth = Body(
        mass=5.972e24,
        position=[149.6, 0],      # 149.6 million km from Sun
        velocity=[0, 2.574],      # ~29.78 km/s converted to million km/day
        radius=5,
        body_type="planet"
    )

    mars = Body(
        mass=6.39e23,
        position=[227.9, 0],
        velocity=[0, 2.077],      # ~24.07 km/s
        radius=4,
        body_type="planet"
    )

    venus = Body(
        mass=4.867e24,
        position=[108.2, 0],
        velocity=[0, 3.022],      # ~34.98 km/s
        radius=5,
        body_type="planet"
    )

    mercury = Body(
        mass=3.285e23,
        position=[57.9, 0],
        velocity=[0, 4.094],      # ~47.36 km/s
        radius=3,
        body_type="planet"
    )

    return [sun, mercury, venus, earth, mars]