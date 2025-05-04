class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sorted_str = sorted(strs)
        first = sorted_str[0]
        last = sorted_str[-1]
        res = ""
        for i in range(len(first)):
            if first[i] != last[i]:
                return res
            res += first[i]
        return res
        # min_str = min(strs, key = len)
        # if not strs:
        #     return ""
        
        # for idx, char in enumerate(min_str):
        #     for word in strs:
        #         if word[idx] != char:
        #             return min_str[:idx]
        # return min_str