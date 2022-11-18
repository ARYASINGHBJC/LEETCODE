class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        # for i in range(2,301):
        #     if i % 2== 0 and i % n == 0:
        #         return i
        return n if n % 2 == 0 else 2*n