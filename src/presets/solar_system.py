from body import Body


from body import Body


def create_solar_system():
    sun = Body(
        mass=10000,
        position=[0, 0],
        velocity=[0, 0],
        radius=15,
        body_type="star"
    )

    planet1 = Body(
        mass=10,
        position=[100, 0],
        velocity=[0, 10],
        radius=5,
        body_type="planet"
    )

    planet2 = Body(
        mass=10,
        position=[150, 0],
        velocity=[0, 8],
        radius=6,
        body_type="planet"
    )

    return [sun, planet1, planet2]