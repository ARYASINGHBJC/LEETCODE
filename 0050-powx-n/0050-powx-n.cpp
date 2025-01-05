class Solution {
public:
    double myPow(double x, int n) {
        double res;
        if(n == 0){
            return 1;
        }
        res = myPow(x, n/2);
        if(n %2 == 0){
            return res * res;
        }else{
            if(n > 0){
                return x * (res * res);
            }else{
                return (res*res)/x;
            }
        }
    }
};