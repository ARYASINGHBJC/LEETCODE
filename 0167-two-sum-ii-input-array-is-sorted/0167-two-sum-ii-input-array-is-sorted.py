class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)
        while l < r:
            if (numbers[l] + numbers[r-1]) == target:
                return [l+1, r]
            elif (numbers[l] + numbers[r-1]) < target:
                l += 1
            else:
                r -= 1
