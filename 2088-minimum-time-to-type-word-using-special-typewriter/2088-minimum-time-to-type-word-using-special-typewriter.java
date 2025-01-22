class Solution {
    public int minTimeToType(String word) {
        char prev = 'a';
        int res = 0;
        for(char ch: word.toCharArray()){
            int diff = Math.abs(prev - ch);
            res += Math.min(diff, 26-diff);
            prev = ch;
        }
        res+= word.length();
        return res;
    }
}