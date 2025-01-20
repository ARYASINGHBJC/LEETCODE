class Solution {
    public int minDifference(int[] nums) {
        Arrays.sort(nums);
        if(nums.length <= 4) return 0;
        int res = Integer.MAX_VALUE;
        for(int l = 0 ; l < 4; l++){
            int r = nums.length - 4 + l;
            res = Math.min(res, nums[r] - nums[l]);
        }
        return res;
    }
}