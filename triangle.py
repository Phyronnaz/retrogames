class Triangle:
    def __init__(self, p0, p1, p2):
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2

    def is_inside(self, position):
        p0x = self.p0[0]
        p0y = self.p0[1]

        p1x = self.p1[0]
        p1y = self.p1[1]

        p2x = self.p2[0]
        p2y = self.p2[1]

        px = position[0]
        py = position[1]

        area = 0.5 * (-p1y * p2x + p0y * (-p1x + p2x) + p0x * (p1y - p2y) + p1x * p2y)

        s = 1 / (2 * area) * (p0y * p2x - p0x * p2y + (p2y - p0y) * px + (p0x - p2x) * py)
        t = 1 / (2 * area) * (p0x * p1y - p0y * p1x + (p0y - p1y) * px + (p1x - p0x) * py)

        return (0 <= s <= 1) and (0 <= t <= 1) and (0 <= s + t <= 1)