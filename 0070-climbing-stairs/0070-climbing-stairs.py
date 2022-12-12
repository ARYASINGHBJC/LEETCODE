# class Solution:
#     @cache
#     def climbStairs(self, n):
#         if n <= 2:
#             return n
#         return self.climbStairs(n-1) + self.climbStairs(n-2)


# class Solution:
#     def climbStairs(self, n):
#         dp = [1, 1]
#         for i in range(2, n+1):
#             dp.append(dp[i-1] + dp[i-2])
#         return dp[n]


# class Solution:
#     def climbStairs(self, n):
#         a = b = 1
#         for _ in range(n):
#             a, b = b, a+ b          
#         return a

class Solution:
    def climbStairs(self, n):
        a = b = 1
        while n:
            a, b = b, a+ b 
            n -= 1
        return a


#TLE
# class Solution:
#     def climbStairs(self, n):
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
#         return self.climbStairs(n-1) + self.climbStairs(n-2)

# class Solution:
#     def __init__(self):
#         self.dic = {1:1, 2:2}

#     def climbStairs(self, n):
#         if n not in self.dic:
#             self.dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
#         return self.dic[n]

