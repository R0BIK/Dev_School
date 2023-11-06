from math import sqrt
class Vector:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def add(self, other_coordinates):
        if len(self.coordinates) != len(other_coordinates.coordinates):
            return("error")

        new_coordinates = []
        for i in range(len(self.coordinates)):
            new_coordinates.append(self.coordinates[i] + other_coordinates.coordinates[i])
        return(Vector(new_coordinates))

    def subtract(self, other_coordinates):
        if len(self.coordinates) != len(other_coordinates.coordinates):
            return ("error")

        new_coordinates = []
        for i in range(len(self.coordinates)):
            new_coordinates.append(self.coordinates[i] - other_coordinates.coordinates[i])
        return(Vector(new_coordinates))


    def dot(self, other_coordinates):
        if len(self.coordinates) != len(other_coordinates.coordinates):
            return ("error")

        new_coordinates = []
        for i in range(len(self.coordinates)):
            new_coordinates.append(self.coordinates[i] * other_coordinates.coordinates[i])
        return(sum(new_coordinates))

    def norm(self):
        new_coordinates = []
        for i in range(len(self.coordinates)):
            new_coordinates.append(pow(self.coordinates[i], 2))
        return(sqrt(sum(new_coordinates)))

    def equals(self, other_coordinates):
        if self.coordinates == other_coordinates.coordinates:
            return(True)

    def __str__(self):
        return(f"({','.join(map(str, self.coordinates))})")
