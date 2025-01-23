class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i , j = 0, 0
        cnt = 0
        g.sort()
        s.sort()
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
                cnt += 1
            j += 1
        return cnt
