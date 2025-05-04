class Solution {
    public String longestCommonPrefix(String[] strs) {
        Arrays.sort(strs);
        String first = strs[0];
        String last = strs[strs.length-1];
        int cnt = 0;
        for(int i = 0; i < Math.min(first.length(), last.length()); i++){
            if(first.charAt(i) == last.charAt(i)){
                cnt++;
            }else{
                break;
            }
        }
        return first.substring(0, cnt);

    //     if(strs == null || strs.length == 0){
    //         return "";
    //     }
    //     Arrays.sort(strs);
    //     String first = strs[0];
    //     String last = strs[strs.length-1];
    //     StringBuilder res = new StringBuilder();
    //     for(int i =0; i < first.length();i++){
    //         if(first.charAt(i) != last.charAt(i)){
    //             return res.toString();
    //         }res.append(first.charAt(i));
    //     }
    //     return res.toString();
    }
}