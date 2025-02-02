class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        for rot_off in range(n):
            check_sorted = []
            for idx in range(rot_off, n):
                check_sorted.append(nums[idx])
            for idx in range(rot_off):
                check_sorted.append(nums[idx])
            is_sorted= True
            for i in range(1, n):
                if(check_sorted[i-1] > check_sorted[i]):
                    is_sorted = False
                    break

            if is_sorted: return True
        return False