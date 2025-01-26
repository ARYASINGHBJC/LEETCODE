class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        cnt = 0
        prefix_sum = 0
        
        for i in range(len(nums) - 1):  # Exclude the last partition
            prefix_sum += nums[i]
            suffix_sum = total_sum - prefix_sum
            
            if abs(prefix_sum - suffix_sum) % 2 == 0:
                cnt+=1
        return cnt