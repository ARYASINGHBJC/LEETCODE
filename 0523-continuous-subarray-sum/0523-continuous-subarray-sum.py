class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        numMap = {0:0}
        sm = 0
        for i in range(len(nums)):
            sm += nums[i]
            if sm % k not in numMap:
                numMap[sm%k] = i + 1
            if numMap[sm % k] < i:
                return True
        return False