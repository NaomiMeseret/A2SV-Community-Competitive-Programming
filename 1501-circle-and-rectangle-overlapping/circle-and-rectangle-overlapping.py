class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        x = 0

        if xCenter < x1:
            x = x1 - xCenter
        elif xCenter > x2:
            x = xCenter - x2

        y = 0

        if yCenter < y1:
            y = y1 - yCenter
        elif yCenter > y2:
            y = yCenter - y2

        return x**2 + y**2 <= radius**2
        