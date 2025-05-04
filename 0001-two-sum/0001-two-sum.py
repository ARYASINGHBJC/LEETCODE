class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hp = {}
        for idx, num in enumerate(nums):
            if target - num in hp:
                return [hp[target - num], idx]
            else:
                hp[num] = idx
        return [-1, -1]
