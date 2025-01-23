class Solution {
    public int minimumMoves(String s) {
        int cnt = 0, ans = 0;
        while(cnt < s.length()){
            if(s.charAt(cnt) == 'X'){
                cnt += 3;
                ans += 1;
            }else{
                cnt += 1;
            }
        }
        return ans;
    }
}