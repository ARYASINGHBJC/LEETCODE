class Solution {
    public static int search(int[] nums, int target, boolean bool){
        int low = 0;
        int high = nums.length -1;
        int bound = -1;
        while(low <= high){
            int mid = (low +high)/2;
            if(nums[mid] == target){
                bound = mid;
                if(bool == true){
                    high = mid -1;
                }else{
                    low = mid+1;
                }
            }else if(nums[mid] < target){
                low = mid + 1;
            }else {
                high = mid - 1;
            }
        }
        return bound;
    } 
    public int[] searchRange(int[] nums, int target) {
        if(nums.length == 0){
            return new int[]{-1,-1};
        }
        boolean bool = true;
        int first = search(nums, target, bool);
        int last = search(nums, target, !bool);
        return new int[] {first, last};
    }
}