class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cntr = Counter(arr)
        cnt = 0
        for ele in arr:
            if cntr[ele] == 1:
                cnt += 1
                if cnt == k:
                    return ele
        return ""
            