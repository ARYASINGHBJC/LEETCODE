class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        mx = 0
        for ele in nums:
            if ele == 1:
                cnt += 1
                mx = max(mx, cnt)
                print(mx)
            else:
                cnt = 0
        return mx
