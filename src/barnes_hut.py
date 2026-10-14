import numpy as np

class QuadTree:
    def __init__(self, cx, cy, half_size):
        # Centre and half-size define the boundary of this node
        self.cx = cx
        self.cy = cy
        self.half_size = half_size

        # The single body this node holds (leaf nodes only)
        self.body = None

        # Centre of mass and total mass for this node
        self.total_mass = 0.0
        self.com = np.zeros(2)  # centre of mass position

        # Four children: NW, NE, SW, SE
        self.NW = None
        self.NE = None
        self.SW = None
        self.SE = None

    def is_leaf(self):
        return self.NW is None

    def contains(self, position):
        # Check if a position falls within this node's boundary
        return (abs(position[0] - self.cx) <= self.half_size and
                abs(position[1] - self.cy) <= self.half_size)

    def subdivide(self):
        # Split this node into four quadrants
        hs = self.half_size / 2
        self.NW = QuadTree(self.cx - hs, self.cy - hs, hs)
        self.NE = QuadTree(self.cx + hs, self.cy - hs, hs)
        self.SW = QuadTree(self.cx - hs, self.cy + hs, hs)
        self.SE = QuadTree(self.cx + hs, self.cy + hs, hs)

    def get_quadrant(self, position):
        # Return the correct child node for a given position
        if position[0] <= self.cx:
            return self.NW if position[1] <= self.cy else self.SW
        else:
            return self.NE if position[1] <= self.cy else self.SE
    
    def insert(self, body):
        # Ignore inactive bodies
        if not body.is_active:
            return

        # Update this node's centre of mass and total mass
        self.com = (self.com * self.total_mass + body.position * body.mass) / (self.total_mass + body.mass)
        self.total_mass += body.mass

        # Case 1: empty leaf node — just store the body here
        if self.body is None and self.is_leaf():
            self.body = body
            return

        # Case 2: leaf node already has a body — subdivide and push both down
        if self.is_leaf():
            self.subdivide()
            # Push existing body into correct quadrant
            self.get_quadrant(self.body.position).insert(self.body)
            self.body = None

        # Case 3: internal node — insert into correct quadrant
        self.get_quadrant(body.position).insert(body)

    def calculate_force(self, body, G, theta=0.5, softening=5.0):
        if not body.is_active:
            return np.zeros(2)
    
        if self.total_mass == 0:
            return np.zeros(2)
    
        # If this is a leaf node containing the same body, skip it
        if self.is_leaf() and self.body is body:
            return np.zeros(2)
    
        direction = self.com - body.position
        distance = np.linalg.norm(direction)
    
        if distance == 0:
            return np.zeros(2)
    
        s = 2 * self.half_size
        if self.is_leaf() or (s / distance) < theta:
            softened_dist = np.sqrt(distance**2 + softening**2)
            force_magnitude = G * body.mass * self.total_mass / softened_dist**2
            return force_magnitude * (direction / distance)
    
        force = np.zeros(2)
        for child in [self.NW, self.NE, self.SW, self.SE]:
            if child is not None:
                force += child.calculate_force(body, G, theta, softening)
    
        return force