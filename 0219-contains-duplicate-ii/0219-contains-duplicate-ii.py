class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        index = {}
        for i, n in enumerate(nums):
            if i - k <= index.get(n):
                return True
            index[n] = i
        return False