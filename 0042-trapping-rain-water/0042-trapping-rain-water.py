class Solution:
    def trap(self, height: List[int]) -> int:
        low = 0
        high = len(height) - 1
        lmax = height[low]
        rmax = height[high]
        res = 0
        while low < high:
            if lmax < rmax:
                low += 1
                lmax = max(lmax, height[low])
                res += (lmax - height[low])
            else:
                high -= 1
                rmax = max(rmax, height[high])
                res += (rmax - height[high])
        return res