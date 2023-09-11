class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) <= 2:
            return True
        (x0, y0) , (x1, y1) = coordinates[0], coordinates[1]
        # (y0 - y1) / x0 - x1 = y1 - y / x1 - x
        a = x1 - x0
        b = y1 - y0
        for x, y in coordinates:
            if (y0 - y) * a != (x0 - x) * b:
                return False
        return True