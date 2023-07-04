# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         d = {}
#         for ele in nums:
#             if ele not in d:
#                 d[ele] = 1
#             else:
#                 d[ele] += 1
#         for key,val in d.items():
#             if val == 1:
#                 return key
class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    ones = 0
    twos = 0

    for num in nums:
      ones ^= (num & ~twos)
      twos ^= (num & ~ones)

    return ones