class Solution {
    public int countPartitions(int[] nums) {
        int sm = 0;
        for(int num:nums){
            sm += num;
        }
        int n = nums.length;
        if(sm % 2 == 0){
            return n -1;
        }
        return 0;
    }
}