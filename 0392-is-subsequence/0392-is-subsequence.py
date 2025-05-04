class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        res = ""
        j = 0
        if not s:
            return True
        for i in range(len(t)):
            if j < len(s):
                if s[j] == t[i]:
                    res += t[i]
                    j += 1
                else:
                    j == len(res)
        return res == s