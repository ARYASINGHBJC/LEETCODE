class Solution {
    public int jump(int[] nums) {
        int ans = 0, n = nums.length;
        int currEnd = 0, currFar = 0;
        for(int i = 0 ; i < n -1 ;i++){
            currFar = Math.max(currFar, i + nums[i]);

            if(i == currEnd){
                ans++;
                currEnd = currFar;
            }
        }
        return ans;
    }
}