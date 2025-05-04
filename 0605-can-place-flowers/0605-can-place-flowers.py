class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        bed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed)+1):
            if (bed[i+1] + bed[i-1] + bed[i]) == 0:
                n -= 1
                bed[i] = 1
        if n <= 0: return True
        return False