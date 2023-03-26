# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         res = len(nums)
#         for i in range(res):
#             res  += (i - nums[i])
#         return res


# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         n = len(nums)
#         return (n*(n+1))//2 - sum(nums)
    
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         res = 0
#         for idx, ele in enumerate(nums):
#             res = res ^ (idx + 1) ^ ele
#         return res
    
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         ele = len(nums)
#         for i in range(len(nums)):    
#             ele = ele ^ i ^ nums[i]
#         return ele


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return reduce(operator.xor, nums)^[n,1,n+1,0][n%4]