class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        maxDistance = 0
        
        for i in range(1, len(colors)):
            if colors[0] != colors[i]:
                maxDistance = max(maxDistance, i)
            if colors[i] != colors[-1]:
                maxDistance = max(maxDistance, len(colors) - i - 1)
            
        return maxDistance


