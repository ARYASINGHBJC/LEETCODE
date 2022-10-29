class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set(nums)
        i = 1
        for i in range(1, len(nums)+1):
            if i in s:
                i += 1
            else:
                return i 
        return len(nums) + 1
        