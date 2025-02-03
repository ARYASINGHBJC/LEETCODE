class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        mxInc = 1
        mxDec = 1
        ans = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                mxInc += 1
                mxDec = 1
            elif nums[i] < nums[i-1]:
                mxInc = 1
                mxDec += 1
            else:
                mxInc = mxDec = 1
            ans = max(mxInc, mxDec, ans)
        return ans if len(nums) > 1 else 1