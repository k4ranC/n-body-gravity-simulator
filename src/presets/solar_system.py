from body import Body


def create_solar_system():
    sun = Body(
        mass=10000,
        position=[0, 0],
        velocity=[0, 0]
    )

    planet1 = Body(
        mass=10,
        position=[100, 0],
        velocity=[0, 10]
    )

    planet2 = Body(
        mass=10,
        position=[150, 0],
        velocity=[0, 8]
    )

    return [sun, planet1, planet2]