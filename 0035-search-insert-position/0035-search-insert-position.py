class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)
        while i < j:
            m = i + (j-i)//2
            if nums[m] == target: return m
            elif nums[m] > target: j = m
            else: i = m+1
                
        return i