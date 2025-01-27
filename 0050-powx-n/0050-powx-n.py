class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        result = 1
        while n:
            if n % 2:  # If n is odd
                result *= x
            x *= x  # Square the base
            n //= 2  # Halve the exponent
        return result
