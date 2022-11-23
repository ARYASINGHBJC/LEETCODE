class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        N = len(matrix)
        st = {i+ 1 for i in range(N)}
        for i in range(N):
            row = set()
            col = set()
            for j in range(N):
                if matrix[i][j] in col or matrix[j][i] in row:
                    return False
                row.add(matrix[j][i])
                col.add(matrix[i][j])
        return True