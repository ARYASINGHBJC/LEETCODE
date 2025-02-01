class Solution {
    public int largestAltitude(int[] gain) {
        int prefix = 0;
        int res = 0;
        for(int g: gain){
            prefix += g;
            res = Math.max(res, prefix);
        }
        return res;
    }
}