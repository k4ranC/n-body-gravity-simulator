from simulator import Simulator
from presets.solar_system import create_solar_system
from presets.black_hole import create_black_hole_system
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Select the preset to simulate
PRESET = "black_hole"
# PRESET = "solar_system"

if PRESET == "solar_system":
    bodies = create_solar_system()
elif PRESET == "black_hole":
    bodies = create_black_hole_system()
else:
    raise ValueError("Unknown preset selected.")

# Initialize the simulator with the created bodies
simulator = Simulator(bodies, gravitational_constant=4.982e-28) # Adjusted G for our scaled units

fig, ax = plt.subplots()

# Set the limits and labels for the plot
ax.set_xlim(-300, 300)
ax.set_ylim(-300, 300)
ax.set_aspect("equal")
ax.set_xlabel("X position")
ax.set_ylabel("Y position")
ax.set_title(f"N-Body Gravity Simulation: {PRESET}")

# Create lists to hold the body dots and their trails
body_dots = []
trails_x = []
trails_y = []
trail_lines = []

def get_body_colour(body):
    if body.body_type == "star":
        return "orange"
    elif body.body_type == "planet":
        return "blue"
    elif body.body_type == "black_hole":
        return "black"
    elif body.body_type == "particle":
        return "gray"
    else:
        return "black"

for body in bodies:
    # Create a dot for the body and a line for its trail
    dot, = ax.plot(
    [],
    [],
    "o",
    markersize=body.radius,
    color=get_body_colour(body)
)
    trail, = ax.plot([], [], linewidth=1)

    # Store the dot and trail for each body
    body_dots.append(dot)
    trail_lines.append(trail)
    trails_x.append([])
    trails_y.append([])

def update(frame):
    simulator.step(1) # change the timestep for faster/slower simulation

    # Update the positions of the bodies and their trails
    for i, body in enumerate(bodies):
        body_dots[i].set_data([body.position[0]], [body.position[1]])

        trails_x[i].append(body.position[0])
        trails_y[i].append(body.position[1])

        trail_lines[i].set_data(trails_x[i], trails_y[i])

    return body_dots + trail_lines

# Create the animation
animation = FuncAnimation(
    fig,
    update,
    frames=5000,
    interval=1,
    blit=True
)

plt.show()