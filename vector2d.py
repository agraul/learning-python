import math


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):  # inclusive addition
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2D(self.x * other.x, self.y * other.y)

    def __imul__(self, other):   # inclusive multiply
        self.x *= other.x
        self.y *= other.y
        return self

    def __truediv__(self, other):
        return Vector2D(self.x / other.x, self.y / other.y)

    def __floordiv__(self, other):
        return Vector2D(self.x // other.x, self.y // other.y)

    def getLength(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalized(self):
        length = self.getLength()
        if length != 0:
            return Vector2D(self.x / length, self.y / length)
        return Vector2D(self)

    def getAngle(self):
        return math.degrees(math.atan2(self.y, self.x))

    def __str__(self):
        return "X: {}\tY: {}".format(self.x, self.y)


def Main():
    vec = Vector2D(5, 6)
    vec2 = Vector2D(2, 3)
    print(vec)
    print(vec2)

    tempmethod = vec.getAngle

    vec = vec + vec2
    print(vec)

    vec += vec2
    print(vec)

    vec *= Vector2D(2, 2)
    print(vec)

    print(vec.normalized())
    print(vec.getAngle())
    print(tempmethod())

if __name__ == '__main__':
    Main()
