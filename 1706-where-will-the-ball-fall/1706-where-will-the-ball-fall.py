class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        colLength = len(grid[0])
        rowLength = len(grid)
        def validate(col):
            for row in range(rowLength):
                if col < colLength-1 and  grid[row][col] + grid[row][col+1] == 2: col += 1 #1, 1
                elif  col > 0 and  grid[row][col] + grid[row][col-1] == -2: col -= 1 #-1, -1
                else: return -1
            return col
        
        return [validate(i) for i in range(colLength)]
        # ans = [0]*len(grid[0])
        # colLength = len(grid[0])
        # rowLength = len(grid)
        # for col in range(colLength):
        #     currentCol = col
        #     for row in range(rowLength):
        #         nextColumn = currentCol + grid[row][currentCol]
        #         if nextColumn < 0 or nextColumn > colLength - 1 or grid[row][currentCol] != grid[row][nextColumn]:
        #             ans[col] = -1
        #             break
        #         ans[col] = nextColumn
        #         currentCol = nextColumn
        # return ans
                        