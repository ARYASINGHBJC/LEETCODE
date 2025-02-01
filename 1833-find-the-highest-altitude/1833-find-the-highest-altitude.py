class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix = 0
        res = 0
        for ele in gain:
            prefix += ele
            res = max(res, prefix)
        return res