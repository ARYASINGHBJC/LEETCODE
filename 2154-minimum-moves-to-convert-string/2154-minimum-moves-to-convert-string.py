class Solution:
    def minimumMoves(self, s: str) -> int:
        cnt = ans = 0
        while cnt < len(s):
            if s[cnt] == 'X':
                cnt += 3
                ans += 1
            else:
                cnt += 1
        return ans