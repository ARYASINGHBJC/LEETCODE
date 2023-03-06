# class Solution:
#     def findKthPositive(self, arr: List[int], k: int) -> int:
#         l, r = 0, len(arr)
#         while l < r:
#             m = (l + r) // 2
#             if (arr[m] - 1 - m) < k:
#                 l = m + 1
#             else:
#                 r = m
#         return l + k
class Solution:
    def findKthPositive(self, a: List[int], k: int) -> int:
        s = set(a)
        cnt = 0
        for i in range(1, max(s)):
            if i not in s:
                cnt += 1
                if cnt == k:
                    return i
        return max(s) + k - cnt 