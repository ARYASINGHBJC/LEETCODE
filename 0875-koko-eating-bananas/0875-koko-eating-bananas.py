class Solution:
    def minEatingSpeed(self,piles: List[int], H: int) -> int:
        left, right = 1, max(piles),
        while left < right:
            mid = left  + (right - left) // 2
            if sum(math.ceil(pile / mid) for pile in piles) <= H:
                right = mid
            else:
                left = mid + 1
        return left    

    
#     def minEatingSpeed(self, piles, h):
#         left = 1
#         right = max(piles)
        
#         while left < right:
#             mid = (left + right) // 2
#             if self.canEatAll(piles, mid, h):
#                 right = mid
#             else:
#                 left = mid + 1
        
#         return left
    
#     def canEatAll(self, piles, speed, h):
#         time = 0
#         for pile in piles:
#             time += (pile - 1) // speed + 1
#             if time > h:
#                 return False
#         return True