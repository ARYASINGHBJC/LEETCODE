class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zero1 = zero2 = 0
        sum1 = sum2 = 0
        for i in range(max(len(nums1), len(nums2))):
            if i < len(nums1):
                if nums1[i] == 0:
                    zero1 += 1
                sum1 += nums1[i]
            if i < len(nums2):
                if nums2[i] == 0:
                    zero2 += 1
                sum2 += nums2[i]
        min1 = sum1 + zero1
        min2 = sum2 + zero2
        # Case A: neither array has zeros → you cannot adjust either
        if zero1 == 0 and zero2 == 0:
            if sum1 != sum2:   # ← you had (zero1==0 or zero2==0) and used the wrong sums
                return -1
        
        # Case B: only nums1 is adjustable, nums2 is fixed
        if zero1 > 0 and zero2 == 0:
            # even at its smallest (min1), nums1 exceeds the fixed sum2 → impossible
            if min1 > sum2:
                return -1
        
        # Case C: only nums2 is adjustable, nums1 is fixed
        if zero2 > 0 and zero1 == 0:
            if min2 > sum1:
                return -1
        return max(min1, min2)
