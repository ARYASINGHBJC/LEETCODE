class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            m = (i) + (j - i)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                i = m  + 1
            else:
                j = m - 1
        return -1