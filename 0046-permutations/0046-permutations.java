class Solution {
    private static void swap(int i, int j, int [] arr){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    private static void getPermutation(int[] arr, int idx, List<List<Integer>>res){
        if(idx == arr.length){
            List<Integer> permutation = new ArrayList<>();
            for(int num: arr){
                permutation.add(num);
            }
            res.add(new ArrayList<>(permutation));
        }else{
            for(int i = idx; i< arr.length; i++){
                swap(i, idx, arr);
                getPermutation(arr, idx+1, res);
                swap(i, idx, arr);
            }
        }
    }
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        getPermutation(nums, 0, res);
        return res;
    }
}