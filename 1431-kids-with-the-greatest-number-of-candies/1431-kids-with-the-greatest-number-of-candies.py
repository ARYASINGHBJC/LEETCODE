class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = max(candies)
        bool_arr = []
        for ele in candies:
            if ele + extraCandies >= mx:
                bool_arr.append(True)
            else:
                bool_arr.append(False)
        return bool_arr
    