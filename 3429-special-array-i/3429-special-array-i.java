class Solution {
    public boolean isArraySpecial(int[] nums) {
        for(int i= 1;i< nums.length;i++){
            if(nums[i-1] % 2 == 0 && nums[i]%2==0 || nums[i-1]% 2==1 && nums[i]%2 == 1){
                return false;
            }
        }
        return true;
    }
}