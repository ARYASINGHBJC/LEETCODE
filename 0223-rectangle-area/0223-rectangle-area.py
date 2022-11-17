class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        #area of a
        a_area = (ay2- ay1) * (ax2 - ax1)
        
        #area of b
        b_area = (by2- by1) * (bx2 - bx1)
        
        #calculate x-overlap
        left = max(ax1, bx1)
        right = min(ax2, bx2)
        x_overlap = right - left
        
        #calculate y-overlap
        top = min(ay2, by2)
        bottom = max(ay1, by1)
        y_overlap = top - bottom
        
        area = 0
        if x_overlap > 0 and y_overlap > 0:
            area = x_overlap * y_overlap
            
        total = a_area + b_area - area
        return total