from body import Body


def create_solar_system():
    # Scale:
    # distance: 1 unit = 1 million km
    # velocity: million km per day
    # time = days
    # mass: in kg
    # radius: in km

    sun = Body(1.989e30, [0, 0], [0, 0], 696340, "star", "Sun")
    mercury = Body(3.285e23, [57.9, 0], [0, 4.094], 2439.7, "planet", "Mercury")
    venus = Body(4.867e24, [108.2, 0], [0, 3.022], 6051.8, "planet", "Venus")
    earth = Body(5.972e24, [149.6, 0], [0, 2.574], 6371, "planet", "Earth")
    mars = Body(6.39e23, [227.9, 0], [0, 2.080], 3389.5, "planet", "Mars")
    jupiter = Body(1.898e27, [778.5, 0], [0, 1.131], 69911, "planet", "Jupiter")
    saturn = Body(5.683e26, [1427, 0], [0, 0.838], 58232, "planet", "Saturn")
    uranus = Body(8.681e25, [2871, 0], [0, 0.588], 25362, "planet", "Uranus")
    neptune = Body(1.024e26, [4495, 0], [0, 0.470], 24622, "planet", "Neptune")
    
    return [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]