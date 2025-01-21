class Solution {
    public int[] productExceptSelf(int[] nums) {
        int [] arr = new int[nums.length];
        for(int i = 0; i< nums.length; i++){
            arr[i] = 1;
        }
        int leftRunPrd = 1, rightRunPrd = 1;
        for(int i= 0;i < nums.length; i++){
            arr[i] = leftRunPrd;
            leftRunPrd *= nums[i];
        }
        for(int i= nums.length-1; i >= 0 ;i--){
            arr[i] *= rightRunPrd;
            rightRunPrd *= nums[i];
        }
        return arr;
    }
}