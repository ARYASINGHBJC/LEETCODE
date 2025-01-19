class Solution {
    public int fib(int n){
        if (n == 0) return 0;
        if (n == 1) return 1;
        int[] arrr = new int[n + 1];
        arrr[0] = 0;
        arrr[1] = 1;
        for (int i = 2; i <= n; i++) {
            arrr[i] = arrr[i - 1] + arrr[i - 2];
        }
        return arrr[n];
    }
}
