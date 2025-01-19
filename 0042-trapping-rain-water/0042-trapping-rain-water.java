class Solution {
    public int trap(int[] height) {
        int low = 0;
        int high = height.length - 1;
        int lmax = height[low];
        int rmax = height[high];
        int res = 0;
        while(low < high){
            if(lmax < rmax){
                low++;
                lmax = Math.max(lmax, height[low]);
                res = res + lmax - height[low];
            }else{
                high--;
                rmax = Math.max(rmax, height[high]);
                res = res + rmax - height[high];
            }
        }
        return res;
    }
}