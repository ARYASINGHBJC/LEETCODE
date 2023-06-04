class Solution:
    def findCircleNum(self, A: List[List[int]]) -> int:
        def union(a,b):
            if (root_a := find(a)) == (root_b := find(b)): return False
            parent[root_b] = root_a
            return True
        def find(e):
            if parent[e] != e:
                parent[e] = find(parent[e])
            return parent[e]
        N = len(A)
        parent = [i for i in range(N)]
        return N - sum(A[i][j] and union(i, j) for i,j in product(range(N), range(N)))
        