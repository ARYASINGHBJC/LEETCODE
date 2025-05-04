class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [None]*len(arr)
        mx = -1
        for i in range(len(arr)-1, -1, -1):
            res[i] = mx
            mx = max(mx, arr[i])
        return res
        # res = []
        # for i in range(0, len(arr)-1):
        #     mx = 0
        #     for j in range(i +1, len(arr)):
        #         mx = max(mx, arr[j])
        #     res.append(mx)
        # res.append(-1)
        # return res