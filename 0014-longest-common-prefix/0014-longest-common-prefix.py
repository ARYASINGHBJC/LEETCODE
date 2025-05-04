class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_str = min(strs, key = len)
        if len(strs) <= 1:
            return strs[0]
        for idx, char in enumerate(min_str):
            for word in strs:
                if word[idx] != char:
                    return min_str[:idx]
        return ""