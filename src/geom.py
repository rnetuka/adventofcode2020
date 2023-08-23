from math import sqrt, cos, sin, radians


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, v):
        return Point(self.x + v.x, self.y + v.y)

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def rotate(self, degrees, s=(0, 0)):
        """Rotates this point by specified number of degrees clockwise. Returns a new point. For anti-clockwise
        rotation, specify the degrees as a negative number.

        It is also possible to specify the center of the rotation as a point S (default is 0, 0)

        :param degrees
        :param s optional center of the rotation provided as either a Point or a simple tuple
        """
        v = vector(s, (0, 0))
        p = self + v
        alpha = -radians(degrees)
        x = p.x * round(cos(alpha)) - p.y * round(sin(alpha))
        y = p.x * round(sin(alpha)) + p.y * round(cos(alpha))
        q = Point(x, y) + (-v)
        self.x = q.x
        self.y = q.y


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return f'v({self.x}, {self.y})'

    def __neg__(self):
        return Vector(-self.x, -self.y)


def vector(a, b) -> Vector:
    a = a if isinstance(a, Point) else Point(a[0], a[1])
    b = b if isinstance(b, Point) else Point(b[0], b[1])
    return Vector(b.x - a.x, b.y - a.y)


if __name__ == '__main__':
    s = Point(0, 0)
    a = s + Vector(10, 4)
    b = a.rotate(180, s)
    print(b)
