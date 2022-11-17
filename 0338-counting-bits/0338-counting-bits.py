class Solution:
    def countBits(self, n: int) -> List[int]:
        # ans = []
        # for i in range(n +1):
        #     ans.append(bin(i).count('1'))
        # return ans
        ans = [0]
        for i in range(1, n +1):
            ans.append(ans[i >> 1]  + (i & 1))
        return ans