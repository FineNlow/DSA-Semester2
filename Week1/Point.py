"""Position calc"""
class Point:
    def __init__(self, x=0, y=0):
        self.set_coordinates(x, y)

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return (self.x, self.y)

    def calculate_distance(self, other_point):
        return ((other_point.x - self.x)**2 + (other_point.y - self.y)**2) ** 0.5

BOSS = Point(float(input()), float(input()))
ART = Point(float(input()), float(input()))
print(f"{BOSS.calculate_distance(ART):.2f}")
