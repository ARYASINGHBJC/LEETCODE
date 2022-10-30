class Solution:
    def numDecodings(self, s: str) -> int:
        # ------------------- Bottom Up -------------
        
        n = len(s)
        dp = [0]*(n+1)
        dp[n] = 1
        for i in range(n-1, -1, -1):
            if s[i] != '0':
                dp[i] = dp[i+1]
            if i+1 < n and '10' <= s[i:i+2] <= '26':
                dp[i] += dp[i+2]
        return dp[0]
        # ---------------- Top Down -----------------
        # if not s or s[0] == '0':return 0
        # dp = [0]*(len(s)+1)
        # dp[0:2] = [1,1]
        # for i in range(2, len(s)+1):
        #     if int(s[i-1:i]) != 0:
        #         dp[i] = dp[i-1]
        #     if 10 <= int(s[i-2:i]) <= 26:
        #         dp[i] += dp[i-2]
        # return dp[-1]
        # dp = [0]*len(s)
        # if not s or s[0] == '0':
        #     return 0
        # dp[0] = 1
        # for i in range(1, len(s)):
        #     if int(s[i]) != 0:
        #         dp[i] = dp[i-1]
        #     if 10 <= int(s[i-1:i+1]) <= 26:
        #         if i > 1:
        #             dp[i] += dp[i-2]
        #         else:
        #             dp[i] += dp[i-1]
        # return dp[-1]
#         if not s or s[0]=='0':
#             return 0
#         dp = [0 for x in range(len(s) + 1)] 
#         # base case initialization
#         dp[0:2] = [1,1]
#         for i in range(2, len(s) + 1): 
#             # One step jump
#             if 0 < int(s[i-1:i]):    #one step
#                 dp[i] = dp[i - 1]
#             # Two step jump
#             if 10 <= int(s[i-2:i]) <= 26: #two step
#                 dp[i] += dp[i - 2]   
#         return dp[-1]