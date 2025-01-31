class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = -1
        last = -1
        for i, ele in enumerate(nums):
            if ele == target and first == -1:
                first = i
                last = i
            if ele == target:
                last = i
        return [first, last]