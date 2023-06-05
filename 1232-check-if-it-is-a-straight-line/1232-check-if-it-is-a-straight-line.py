class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        numerator = coordinates[0][0] - coordinates[1][0]
        denominator = coordinates[0][1] - coordinates[1][1]
        for i in range(len(coordinates)):
            x = coordinates[i][0]
            y = coordinates[i][1]
            if (numerator * (y-coordinates[1][1]) != denominator * (x - coordinates[1][0])):
                return False
        return True