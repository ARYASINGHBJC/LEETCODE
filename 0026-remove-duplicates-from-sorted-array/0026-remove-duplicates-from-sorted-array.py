class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 1
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[slow] = nums[i]
                slow += 1
        return slow