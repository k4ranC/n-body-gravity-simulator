from simulator import Simulator
from presets.solar_system import create_solar_system
from presets.black_hole import create_black_hole_system
from visualiser import run_visualisation

# Select the preset to run
# PRESET = "black_hole"
PRESET = "solar_system"

#  Create the bodies based on the selected preset
if PRESET == "solar_system":
    bodies = create_solar_system()
elif PRESET == "black_hole":
    bodies = create_black_hole_system()
else:
    raise ValueError("Unknown preset selected.")

# Create the simulator with the bodies and a scaled gravitational constant
simulator = Simulator(
    bodies,
    gravitational_constant=4.982e-28
)

# Run the visualisation for the selected preset
run_visualisation(simulator, bodies, PRESET)