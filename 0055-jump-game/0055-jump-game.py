class Solution:
    def canJump(self, nums: List[int]) -> bool:
        idx = 0
        for i, ele in enumerate(nums):
            if i > idx:
                return False
            idx = max(idx, i + ele)
        return True 