public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int res = 0;
        for(int i = 0; i < 32; i++){
            int getBit = (n >> i) & 1;
            res |= getBit << (31 - i);
        }
        return res;
    }
}