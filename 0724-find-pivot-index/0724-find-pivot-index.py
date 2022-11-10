class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        totalLength = len(nums)
        currSum = 0
        for i in range(totalLength):
            if currSum == totalSum - currSum - nums[i]: return i
            else: currSum += nums[i]
        return -1