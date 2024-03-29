import math

class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def diameter(self):
        return 2 * self.radius

    def circumference(self):
        return 2 * math.pi * self.radius

    def volume(self):
        return (4/3) * math.pi * (self.radius ** 3)

radius = float(input("Enter the radius of the sphere: "))
my_sphere = Sphere(radius)
print("Diameter of the sphere:", my_sphere.diameter())
print("Circumference of the sphere:", my_sphere.circumference())
print("Volume of the sphere:", my_sphere.volume())
