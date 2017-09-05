class Triangle(object):
    def __init__(self, p0, p1, p2):
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2

    def __getitem__(self, key):
        if key == 0:
            return self.p0
        elif key == 1:
            return self.p1
        elif key == 2:
            return self.p2
        else:
            raise IndexError("index out of bound")

    def is_inside(self, position):
        p0x = self.p0[0]
        p0y = self.p0[1]

        p1x = self.p1[0]
        p1y = self.p1[1]

        p2x = self.p2[0]
        p2y = self.p2[1]

        px = position[0]
        py = position[1]

        area = 0.5 * (-p1y * p2x + p0y * (-p1x + p2x) +
                      p0x * (p1y - p2y) + p1x * p2y)

        s = 1 / (2 * area) * (p0y * p2x - p0x * p2y +
                              (p2y - p0y) * px + (p0x - p2x) * py)
        t = 1 / (2 * area) * (p0x * p1y - p0y * p1x +
                              (p0y - p1y) * px + (p1x - p0x) * py)

        return (0 <= s <= 1) and (0 <= t <= 1) and (0 <= s + t <= 1)

    def some_inside(self, positions):
        return any(map(lambda x: self.is_inside(x), positions))
        """for e in positions:
            if self.is_inside(e):
                return True
        return False"""

    def every_inside(self, positions):
        return all(map(lambda x: self.is_inside(x), positions))
        """for e in positions:
            if not self.is_inside(e):
                return False
        return True"""

"""
print(Triangle((0, 0), (10, 0), (0, 10)).is_inside((1, 1)))
print(
    Triangle(
        (0, 0), (10, 0), (0, 10)).some_inside(((100, 100), (10, 10))))
        """
