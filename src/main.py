import pygame

from simulator import Simulator
from presets.solar_system import create_solar_system
from presets.black_hole import create_black_hole_system
from renderer import Renderer


PRESET = "solar_system"
# PRESET = "black_hole"

if PRESET == "solar_system":
    bodies = create_solar_system()
elif PRESET == "black_hole":
    bodies = create_black_hole_system()
else:
    raise ValueError("Unknown preset")


simulator = Simulator(
    bodies,
    gravitational_constant=4.982e-28 # Adjusted gravitational constant for better visualization
)

renderer = Renderer()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        renderer.handle_event(event)

    renderer.handle_input()

    simulator.step(1)
    renderer.draw(bodies)
    renderer.tick()

pygame.quit()