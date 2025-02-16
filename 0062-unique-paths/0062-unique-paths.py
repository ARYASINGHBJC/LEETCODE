class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def totalPath(i, j, m, n):
            if i == m or j == n:
                return 0
            if i == m - 1 or j == n - 1:
                return 1
            right = totalPath(i+1, j, m, n)
            down = totalPath(i, j+1, m, n)
            return right + down
        return totalPath(0, 0, m, n)