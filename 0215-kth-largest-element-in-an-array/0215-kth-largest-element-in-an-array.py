class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-n for n in nums]
        heapq.heapify(heap)
        for i in range(k):
            res = heapq.heappop(heap)
        return -res
        # nums.sort(reverse= True)
        # return nums[k-1]
