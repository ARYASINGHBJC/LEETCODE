class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
        # hp = defaultdict(int)
        # for num in nums:
        #     hp[num] += 1
        # for key, val in hp.items():
        #     if val > 1:
        #         return True
        # return False