class Solution {
    public double myPow(double x, int n) {
        // if(n == -2147483648){
        //     return 0.00000;
        // }
        long exp = n;
        if(exp < 0){
            exp = -exp;
            x= 1/x;
        }
        double res = 1;
        while(exp > 0) {
            if (exp % 2 == 1){
                res = res * x;
            }
            x = x* x;
            exp = exp /2;
        }
        return res;
    }
}