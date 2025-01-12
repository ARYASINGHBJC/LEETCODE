class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int cnt = 0;
        int res = 0;
        for(int num:nums){
            if(num == 1){
                res = res + 1;
                cnt = Math.max(cnt, res);
            }else{
                res = 0;
            }
        }
        return cnt;
    }
}