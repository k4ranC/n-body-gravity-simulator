import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Get the colour for a body based on its type
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

# Run the visualisation for a given simulator and preset name
def run_visualisation(simulator, bodies, preset_name):
    fig, ax = plt.subplots()

    # Set up the plot limits and labels
    ax.set_xlim(-5000, 5000)
    ax.set_ylim(-5000, 5000)
    ax.set_aspect("equal")
    ax.set_xlabel("X position")
    ax.set_ylabel("Y position")
    ax.set_title(f"N-Body Gravity Simulation: {preset_name}")

    # Create lists to hold the body dots and their trails
    body_dots = []
    trails_x = []
    trails_y = []
    trail_lines = []

    # Create a dot and trail for each body
    for body in bodies:
        dot, = ax.plot(
            [],
            [],
            "o",
            markersize=body.radius,
            color=get_body_colour(body)
        )

        trail, = ax.plot([], [], linewidth=1)

        body_dots.append(dot)
        trail_lines.append(trail)
        trails_x.append([])
        trails_y.append([])

    # Update function for the animation
    def update(frame):
        # One day per frame, adjust for faster/slower simulation
        simulator.step(1)

        # Update the positions of the bodies and their trails
        for i, body in enumerate(bodies):
            if not body.is_active:
                body_dots[i].set_data([], [])
                trail_lines[i].set_data([], [])
                continue

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
        blit=True # optimize performance by only redrawing changed elements
    )

    plt.show()