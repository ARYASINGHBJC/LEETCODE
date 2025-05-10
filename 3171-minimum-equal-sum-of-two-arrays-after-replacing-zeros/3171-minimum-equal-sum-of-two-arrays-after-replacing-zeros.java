class Solution {
    public long minSum(int[] nums1, int[] nums2) {
        int n1 = nums1.length;
        int n2 = nums2.length;
        int zero1 = 0;
        long sm1 = 0;
        int zero2 = 0;
        long sm2 = 0;
        for(int i=0; i< Math.max(n1, n2); i++){
            if(i < n1){
                if(nums1[i] == 0){
                    zero1++;
                }else{
                    sm1 += nums1[i];
                }
            }
            if(i < n2){
                if(nums2[i] == 0){
                    zero2++;
                }else{
                    sm2 += nums2[i];
                }
            }
        }
        long min1 = sm1 + zero1;
        long min2 = sm2 + zero2;
        if(zero1 == 0){
            if(min2 > sm1){
                return -1;
            }
        }
        if(zero2 == 0){
            if(min1 > sm2){
                return -1;
            }
        }
        return Math.max(min1, min2);
    }
}