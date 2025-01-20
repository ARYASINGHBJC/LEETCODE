class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxPrdct = minPrdct = ans = nums[0]
        for ele in nums[1:]:
            if ele < 0 :
                maxPrdct, minPrdct = minPrdct, maxPrdct
            
            maxPrdct = max(ele, maxPrdct * ele)
            minPrdct = min(ele, minPrdct * ele)
            ans = max(ans, maxPrdct)
        return ans