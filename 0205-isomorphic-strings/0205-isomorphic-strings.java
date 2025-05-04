class Solution {
    public boolean isIsomorphic(String s, String t) {
        int[] m1 = new int[256];
        int [] m2 = new int[256];
        for(int i= 0; i< s.length();i++){
            char curr_s = s.charAt(i);
            char curr_t = t.charAt(i);
            if(m1[curr_s] != m2[curr_t]){
                return false;
            }
            m1[curr_s] = i +1;
            m2[curr_t] = i +1;
        }
        return true;
    }
}