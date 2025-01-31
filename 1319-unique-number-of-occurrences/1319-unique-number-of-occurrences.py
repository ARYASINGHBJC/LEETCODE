class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        st = set(arr)
        cnt = set()
        for ele in st:
            if arr.count(ele) not in cnt:
                cnt.add(arr.count(ele))
            else:
                return False
        return True