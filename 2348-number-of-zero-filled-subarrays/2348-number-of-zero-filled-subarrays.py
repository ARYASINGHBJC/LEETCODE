class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        c1 = 0
        c0= 0
        sm = 0
        for ele in nums:
            if ele == 0:
                c1 += 1
            else:
                c0 += 1
                sm += (c1*(c1+1))//2
                c1 = 0
        return sm + (c1*(c1+1))//2