class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        A = nums1
        B = nums2
        if len(nums1) > len(nums2):
            A, B = B, A
        totalLength = len(A) + len(B)
        half = totalLength // 2
        low, high = 0, len(A) - 1
        while True:
            mid = (low + high) >> 1
            partition = half - mid - 2
            Aleftmin = A[mid] if mid >= 0 else float('-inf')
            Arightmin = A[mid+1] if (mid+1) < len(A) else float('inf')
            Bleftmax = B[partition] if partition >= 0 else float('-inf')
            Brightmax = B[partition + 1] if (partition+1) < len(B) else float('inf')
            
            if Aleftmin <= Brightmax and Bleftmax <= Arightmin:
                if totalLength % 2:
                    return min(Arightmin, Brightmax)
                return (max(Aleftmin, Bleftmax) + min(Arightmin, Brightmax)) / 2
            elif Aleftmin > Brightmax:
                high = mid - 1
            else:
                low = mid + 1
#         A = nums1
#         B= nums2
#         if len(nums1) > len(nums2):
#             A, B = B, A
#         totalLength = len(A) + len(B)
#         half = totalLength // 2
#         low = 0
#         high = len(A) - 1
#         while True:
#             mid = (low+high)//2
#             partition = half - mid -2
#             Aleftmin = A[mid] if mid >= 0 else float('-inf')
#             Arightmin = A[mid + 1] if (mid + 1) < len(A) else float("infinity")
#             Bleftmax = B[partition] if partition >= 0 else float("-infinity")
#             Brightmax = B[partition + 1] if (partition + 1) < len(B) else float("infinity")

#             # partition is correct
#             if Aleftmin <= Brightmax and Bleftmax <= Arightmin:
#                 # odd
#                 if totalLength % 2:
#                     return min(Arightmin, Brightmax)
#                 # even
#                 return (max(Aleftmin, Bleftmax) + min(Arightmin, Brightmax)) / 2
#             elif Aleftmin > Brightmax:
#                 high = mid - 1
#             else:
#                 low = mid + 1
#         if len(nums1) > len(nums2):
#             nums1, nums2 = nums2, nums1
        
#         m, n = len(nums1), len(nums2)
        
#         left_size = (m + n + 1) // 2
#         start = 0
#         end = m
#         is_even = ((m + n) % 2) == 0
#         while start <= end:
#             a_part = (start + end) // 2
#             b_part = left_size - a_part
            
#             aleftmax = float("-inf") if a_part == 0 else nums1[a_part - 1]
#             arightmin = float("inf") if a_part == m else nums1[a_part]
#             bleftmax = float("-inf") if b_part == 0 else nums2[b_part - 1]
#             brightmin = float("inf") if b_part == n else nums2[b_part]
            
#             if aleftmax <= brightmin and bleftmax <= arightmin:
#                 if not is_even:
#                     return max(aleftmax, bleftmax)
#                 else:
#                     return (max(aleftmax, bleftmax) + min(arightmin, brightmin))/ 2
#             elif aleftmax > brightmin:
#                 end = a_part - 1
#             elif bleftmax > arightmin:
#                 start = a_part + 1
            
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         i = 0
#         j = 0
#         k = 0
#         arr = []
#         while i< len(nums1) and j < len(nums2):
# 	        if nums1[i] <= nums2[j]:
# 		        arr.append(nums1[i])
# 		        i += 1
# 	        else:
# 		        arr.append(nums2[j])
# 		        j += 1
		
#         while i<len(nums1):
# 	        arr.append(nums1[i])
# 	        i += 1
#         while j < len(nums2):
# 	        arr.append(nums2[j])
# 	        j += 1
#         print(arr)
#         a = 0
#         b = len(arr)
#         if len(arr) % 2 != 0:
#             m = a + (b-a)// 2
#             return arr[m]
#         else:
#             m1 = a + (b-a)//2 
#             m2 = a + (b-a)//2 - 1
#             return ((arr[m1] + arr[m2])/2)

