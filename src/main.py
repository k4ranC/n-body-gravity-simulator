from body import Body
from simulator import Simulator
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the bodies in the simulation
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
    mass=50,
    position=[150, 0],
    velocity=[0, 8]
)

# Create the simulator with the defined bodies
simulator = Simulator([sun, planet1, planet2])

# Set up the plot
fig, ax = plt.subplots()

# Set limits and labels
ax.set_xlim(-200, 200)
ax.set_ylim(-200, 200)
ax.set_aspect("equal")
ax.set_xlabel("X position")
ax.set_ylabel("Y position")
ax.set_title("N-Body Gravity Simulation")

# Initialize plot elements for the sun and planets
sun_dot, = ax.plot([], [], "o", markersize=10)
planet1_dot, = ax.plot([], [], "o", markersize=5)
planet2_dot, = ax.plot([], [], "o", markersize=5)

# Trails for planets
planet1_trail_x = []
planet1_trail_y = []
planet2_trail_x = []
planet2_trail_y = []

# Initialize plot elements for trails
planet1_trail, = ax.plot([], [])
planet2_trail, = ax.plot([], [])

# Update function for animation
def update(frame):
    simulator.step(0.01)  # change timestep here for faster/slower simulation

    # Update positions of the sun and planets
    sun_dot.set_data([sun.position[0]], [sun.position[1]])
    planet1_dot.set_data([planet1.position[0]], [planet1.position[1]])
    planet2_dot.set_data([planet2.position[0]], [planet2.position[1]])

    # Update trails for planets
    planet1_trail_x.append(planet1.position[0])
    planet1_trail_y.append(planet1.position[1])
    planet2_trail_x.append(planet2.position[0])
    planet2_trail_y.append(planet2.position[1])

    # Update trail data for plotting
    planet1_trail.set_data(planet1_trail_x, planet1_trail_y)
    planet2_trail.set_data(planet2_trail_x, planet2_trail_y)

    # Return the updated plot elements for blitting optimization
    return sun_dot, planet1_dot, planet2_dot, planet1_trail, planet2_trail

# Create animation
animation = FuncAnimation(fig, update, frames=5000, interval=10, blit=True)

plt.show()