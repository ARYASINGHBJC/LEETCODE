class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left, right = 0, 0
        res = 0
        while right < len(s):
            if s[right] in seen:
                left = max(left, seen[s[right]] + 1)
            seen[s[right]] = right
            res = max(res, right - left + 1)
            right += 1
        return res