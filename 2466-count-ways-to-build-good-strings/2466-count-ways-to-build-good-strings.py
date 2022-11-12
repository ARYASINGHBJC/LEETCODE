class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        dp = [0]*(high+1)
        dp[0] = 1
        for i in range(high):
            if i+zero <= high :
                dp[i+zero] += dp[i]
            if i+one <= high :
                dp[i+one] += dp[i]
        return sum(dp[low:high+1])%mod
#         MOD = 1_000_000_007
#         @lru_cache(100*100)
#         def dp(c):
#             if c == high:
#                 return 1
#             if c > high:
#                 return 0
            
#             if c >= low:
#                 return 1 + dp(c + zero) + dp(c + one)
#             else:
#                 return dp(c + zero) + dp(c + one)
        
#         return dp(0) % MOD