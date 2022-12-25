# class Solution:
#     def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
#         # Get the prefix sum array of the sorted 'nums'.
#         nums.sort()
#         for i in range(1, len(nums)):
#             nums[i] += nums[i - 1]
        
#         answer = []
        
#         # For each query, find its insertion index to the prefix sum array.
#         for query in queries:
#             index = bisect.bisect_right(nums, query)
#             answer.append(index)
            
#         return answer
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # Sort 'nums'
        nums.sort()
        ans = []

        # For each query, collect numbers from lowest to highest.
        # If their sum exceeds the limit 'query', move on to the next query.
        for query in queries:
            count = 0
            for num in nums:
                if query >= num:
                    query -= num
                    count += 1
                else:
                    break
            ans.append(count)
        
        return ans
        