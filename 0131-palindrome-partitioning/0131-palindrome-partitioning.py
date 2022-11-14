class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]
        res = []
        def pal(s):
            return s == s[::-1]
        def dfs(s, valid, res):
            if not s:
                res.append(valid)
                return
            for i in range(1, len(s) + 1):
                if pal(s[:i]):
                    dfs(s[i:] ,valid + [s[:i]], res)
            
        dfs(s, [], res)
        return res