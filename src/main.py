import pygame

from simulator import Simulator
from presets.solar_system import create_solar_system
from presets.black_hole import create_black_hole_system
from renderer import Renderer


PRESET = "solar_system"
# PRESET = "black_hole"

def load_preset(preset_name):
    if preset_name == "solar_system":
        return create_solar_system()

    elif preset_name == "black_hole":
        return create_black_hole_system()

    else:
        raise ValueError("Unknown preset")

bodies = load_preset(PRESET)


simulator = Simulator(
    bodies,
    gravitational_constant=4.982e-28 # Adjusted gravitational constant for better visualization
)

renderer = Renderer()

paused = False
physics_timestep = 1
steps_per_frame = 1

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        renderer.handle_event(event)

        if event.type == pygame.KEYDOWN:

            # Pause / Play
            if event.key == pygame.K_SPACE:
                paused = not paused

            # Speed up
            elif event.key == pygame.K_EQUALS:
                steps_per_frame = min(steps_per_frame * 2, 16)

            # Slow down
            elif event.key == pygame.K_MINUS:
                steps_per_frame = max(1, steps_per_frame // 2)

            # Reset simulation
            elif event.key == pygame.K_r:
                bodies = load_preset(PRESET)

                simulator = Simulator(
                    bodies,
                    gravitational_constant=4.982e-28
                )

    renderer.handle_input()

    if not paused:
        for _ in range(steps_per_frame):
            simulator.step(physics_timestep)
    renderer.draw(bodies)
    renderer.tick()

pygame.quit()