class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> res = new ArrayList<>();
        for(int i = 0; i< numRows ;i++){
            List<Integer> temp = new ArrayList<>();
            for(int j = 0; j < i+1; j++){
                if(j == 0 || j == i){
                    temp.add(1);
                }else{
                    List<Integer> prev =res.get(i-1);
                    int sum = prev.get(j - 1) + prev.get(j);
                    temp.add(sum);
                }
            }
            res.add(temp);
        }
        return res;
    }
}