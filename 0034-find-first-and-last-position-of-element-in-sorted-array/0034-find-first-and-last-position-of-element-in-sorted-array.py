class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]  
        def findBound(isFirst):
            low, high = 0, len(nums) - 1
            bound = -1    
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    bound = mid
                    if isFirst:
                        high = mid - 1  # Search left for first occurrence
                    else:
                        low = mid + 1   # Search right for last occurrence
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return bound       
        first = findBound(True)
        last = findBound(False)
        return [first, last]
