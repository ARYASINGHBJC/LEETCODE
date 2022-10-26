class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # initialize the hash map with index 0 for sum 0
        hash_map = {0: 0}
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            # if the remainder s % k occurs for the first time
            if s % k not in hash_map:
                hash_map[s % k] = i + 1
            # if the subarray size is at least two
            elif hash_map[s % k] < i:
                return True
        return False