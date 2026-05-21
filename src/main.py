from body import Body
from simulator import Simulator

sun = Body(
    mass=10000,
    position=[0, 0],
    velocity=[0, 0]
)

planet = Body(
    mass=10,
    position=[100, 0],
    velocity=[0, 10]
)

simulator = Simulator([sun, planet])

for step in range(10):
    simulator.step(0.01)
    print("Planet position:", planet.position)