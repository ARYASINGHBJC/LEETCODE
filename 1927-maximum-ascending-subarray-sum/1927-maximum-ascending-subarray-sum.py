class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        currSum = nums[0]
        mxSum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                currSum = max(currSum, currSum+nums[i])
                mxSum = max(currSum , mxSum)
            else:
                currSum = nums[i]
        return mxSum