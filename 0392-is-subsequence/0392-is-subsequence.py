class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        cnt =0
        j = 0
        if not s:
            return True
        for i in range(len(t)):
            if j < len(s):
                if s[j] == t[i]:
                    cnt += 1
                    j += 1
        return cnt == len(s)