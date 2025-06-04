class Point3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Point3D(x={self.x}, y={self.y}, z={self.z})"

    def distance_to(self, other):
        """Calculate the Euclidean distance to another Point3D."""
        return ((self.x - other.x) ** 2 + 
                (self.y - other.y) ** 2 + 
                (self.z - other.z) ** 2) ** 0.5

    def translate(self, dx, dy, dz):
        """Translate the point by given deltas."""
        self.x += dx
        self.y += dy
        self.z += dz