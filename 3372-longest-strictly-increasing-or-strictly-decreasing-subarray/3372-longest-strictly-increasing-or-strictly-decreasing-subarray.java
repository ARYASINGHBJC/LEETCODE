class Solution {
    public int longestMonotonicSubarray(int[] nums) {
        int Inc = 1;
        int Dec = 1;
        int ans = 0;
        int n = nums.length;
        if(n==1){
            return 1;
        }
        for(int i= 1; i< n; i++){
            if(nums[i] < nums[i-1]){
                Dec += 1;
                Inc =1;   
            }else if(nums[i] > nums[i-1]){
                Dec =1;
                Inc += 1;
            }else{
                Dec = 1;
                Inc = 1;
            }
            ans = Math.max(ans, Math.max(Inc, Dec));
        }
        return ans;
    }
}