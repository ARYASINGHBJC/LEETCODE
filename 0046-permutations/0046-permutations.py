class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(left, right, arr, res):
            if(left == right):
                res.append(arr.copy())
            else:
                for i in range(left, right):
                    arr[left], arr[i] = arr[i], arr[left]
                    helper(left +1, right, arr,res)
                    arr[left], arr[i] = arr[i], arr[left]
        helper(0, len(nums), nums, res)
        return res
