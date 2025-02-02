class Solution {
    public boolean check(int[] nums) {
        int n = nums.length;
        if(n <= 1){
            return true;
        }
        int invCnt = 0;
        for(int i = 1; i< n; i++){
            if(nums[i] < nums[i-1]){
                invCnt += 1;
            }
        }
        if(nums[0] < nums[n-1]){
            invCnt += 1;
        }
        return invCnt <= 1;
    }
}