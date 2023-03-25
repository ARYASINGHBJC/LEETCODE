class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        # Build the adjacency list of the graph
        adjList = [[] for _ in range(n)]
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        visited = [False] * n
        sizes = [0] * n
        for i in range(n):
            if not visited[i]:
                sizes[i] = self.dfs(i, adjList, visited)

        ans = 0
        sum = 0
        for size in sizes:
            ans += sum * size
            sum += size

        return ans

    def dfs(self, u: int, adjList: List[List[int]], visited: List[bool]) -> int:
        visited[u] = True
        size = 1
        for v in adjList[u]:
            if not visited[v]:
                size += self.dfs(v, adjList, visited)
        return size