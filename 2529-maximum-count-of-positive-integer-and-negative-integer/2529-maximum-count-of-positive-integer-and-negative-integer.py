class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        mx = 0
        mn = 0
        for ele in nums:
            if ele > 0 :
                mx += 1
            elif ele < 0:
                mn += 1
            else:
                continue
        return max(mx , mn)