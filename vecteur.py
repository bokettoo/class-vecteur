import math
class Vecteur2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def str(self):
        return str(self.x) + str(self.y)

    def eq(self, other_vector):
        return self.x == other_vector.x and self.y == other_vector.y

    def norm(self):
        return math.sqrt(self.x**2 + self.y**2)

class Vecteur3D(Vecteur2D):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self.z = z

    def str(self):
        return str(self.x) + str(self.y) + str(self.z)

    def eq(self, other_vector):
        return super().eq(other_vector) and self.z == other_vector.z

    def norm(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)


