class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Hash map 'basket' to store the types of fruits.
        basket = {}
        left = 0
        
        # Add fruit from the right index (right) of the window.
        for right, fruit in enumerate(fruits):
            basket[fruit] = basket.get(fruit, 0) + 1

            # If the current window has more than 2 types of fruit,
            # we remove one fruit from the left index (left) of the window.
            if len(basket) > 2:
                basket[fruits[left]] -= 1

                # If the number of fruits[left] is 0, remove it from the basket.
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
        
        # Once we finish the iteration, the indexes left and right 
        # stands for the longest valid subarray we encountered.
        return right - left + 1
# class Solution:
#     def totalFruit(self, fruits: List[int]) -> int:
#         # Maximum number of fruits we can pick
#         max_picked = 0
        
#         # Iterate over all subarrays: left index left, right index right.
#         for left in range(len(fruits)):
#             for right in range(left, len(fruits)):
#                 # Use a set to count the type of fruits.
#                 basket = set()
                
#                 # Iterate over the current subarray (left, right).
#                 for current_index in range(left, right + 1):
#                     basket.add(fruits[current_index])
                    
#                 # If the number of types of fruits in this subarray (types of fruits) 
#                 # is no larger than 2, this is a valid subarray, update 'max_picked'.
#                 if len(basket) <= 2:
#                     max_picked = max(max_picked, right - left + 1)
        
#         # Return 'max_picked' as the maximum length (maximum number of fruits we can pick).
#         return max_picked
        