class Solution:
    # def helper(self, idx, jumps, nums):
    #     if idx >= len(nums) -1:
    #         return jumps
    #     if nums[idx] == 0:
    #         return float('inf')
    #     mn = float('inf')
    #     for i in range(1, nums[idx] + 1):
    #         mn = min(mn, self.helper(idx+i, jumps+1, nums))
    #     return mn
    def jump(self, nums: List[int]) -> int:
        ans,n = 0, len(nums)
        curr_end, curr_far = 0, 0
        for i in range(n-1):
            curr_far = max(curr_far, i+nums[i])
            if i == curr_end:
                ans += 1
                curr_end = curr_far
        return ans  
        # return self.helper(0,0, nums)
        
        