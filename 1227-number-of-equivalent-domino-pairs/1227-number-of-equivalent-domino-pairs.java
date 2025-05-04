class Solution {
    public int numEquivDominoPairs(int[][] dominoes) {
        int[] count = new int[100];  
        int pairs = 0;

        for (int[] domino : dominoes) {
            int a = domino[0];
            int b = domino[1];
            int key = a < b ? a * 10 + b : b * 10 + a;

            pairs += count[key];     
            count[key]++;        
        }

        return pairs;
    }
}
