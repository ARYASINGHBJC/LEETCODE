class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int l = 0;
        int r = numbers.length;
        while(l < r){
        if(numbers[l] + numbers[r-1] == target){
            return new int [] {l + 1, r};
        }else if (numbers[l] + numbers[r-1] < target){
            l++;
        }else{
            r--;
        }
    }
    return new int [] {};
    }
}