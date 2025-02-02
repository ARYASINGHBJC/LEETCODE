class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq= {}
        for num in nums:
            if num %  2 == 0:
                if num in freq:
                    freq[num] += 1
                else:
                    freq[num] = 1
        count = 0
        res = -1
        for key in freq:
            if freq[key] > count:
                count = freq[key]
                res = key
            elif freq[key] == count:
                if res > key:
                    res = key
        return res