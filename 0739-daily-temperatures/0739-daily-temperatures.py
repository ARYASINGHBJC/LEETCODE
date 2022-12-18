class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans, n = [0]*len(temperatures), len(temperatures)
        for cur in range(n-2,-1,-1):
            nxt = cur+1
            while nxt < n and temperatures[nxt] <= temperatures[cur]:
                nxt += ans[nxt] if ans[nxt] else n
            ans[cur] = nxt-cur if nxt < n else 0
        return ans