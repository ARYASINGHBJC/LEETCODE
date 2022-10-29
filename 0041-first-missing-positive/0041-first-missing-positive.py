class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set(nums)
        n = 1
        for i in range(1, len(nums)+1):
            if n in s:
                n += 1
            else:
                return n 
        return len(nums) + 1
        