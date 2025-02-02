class Solution {
    public int mostFrequentEven(int[] nums) {
        HashMap<Integer, Integer> seen = new HashMap<>();
        for(int i= 0; i< nums.length; i++){
            if(nums[i] % 2 == 0){
                seen.put(nums[i], seen.getOrDefault(nums[i], 0) + 1);
            }
        }
        int cnt = 0;
        int res = -1;
        for(int ele: seen.keySet()){
            if(seen.get(ele) > cnt){
                cnt = seen.get(ele);
                res = ele;
            }
            else if(seen.get(ele) == cnt){
                if(res > ele){
                    res = ele;
                }
            }
        }
        return res;
    }
}