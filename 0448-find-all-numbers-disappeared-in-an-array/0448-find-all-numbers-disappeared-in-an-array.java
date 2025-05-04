class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> ans = new ArrayList<>();
        for(int num: nums){
            nums[Math.abs(num)-1] = -Math.abs(nums[Math.abs(num)-1]); 
        }
        // for(int num:nums){
        //     System.out.println(num);
        // }
        for(int i = 0; i< nums.length; i++){
            if(nums[i] > 0){
                ans.add(i+1);
            }
        }
        return ans;
    }
}