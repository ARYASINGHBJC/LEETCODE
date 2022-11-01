class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ans = [-1]*len(grid[0])
        colLength = len(grid[0])
        rowLength = len(grid)
        for col in range(colLength):
            currentCol = col
            for row in range(rowLength):
                nextColumn = currentCol + grid[row][currentCol]
                if nextColumn < 0 or nextColumn > colLength - 1 or grid[row][currentCol] != grid[row][nextColumn]:
                    ans[col] = -1
                    break
                ans[col] = nextColumn
                currentCol = nextColumn
        return ans
                        