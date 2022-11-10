class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        totalSum = sum(arr)
        if totalSum % 3 != 0: return False
        currSum = 0
        count = 0
        targetSum = totalSum // 3
        for ele in arr:
            currSum += ele
            if currSum == targetSum:
                count += 1
                currSum = 0
        return count >= 3
                