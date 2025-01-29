class Solution {
    public int minOperations(int[] nums) {
        int chng = 0;
        int cnt = 0;
        for (int i =1; i< nums.length; i++){
            if(nums[i] <= nums[i-1]){
                chng = nums[i-1] - nums[i] + 1;
                cnt += chng;
                nums[i] += chng;
            }
        }
        return cnt; 
    }
}