class Solution:
    def fib(self, n: int) -> int:
        first,second = 0, 1
        for i in range(n):
            curr = first + second
            first, second = second, curr
        return first