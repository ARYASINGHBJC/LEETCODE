class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(idx):
            if idx == len(nums):
                res.append(nums[::])
                return
            lookup = set()
            for i in range(idx, len(nums)):
                if nums[i] not in lookup:
                    nums[idx], nums[i] = nums[i], nums[idx]
                    backtrack(idx+1)
                    nums[idx], nums[i] = nums[i], nums[idx]
                    lookup.add(nums[i])
        backtrack(0)
        return res