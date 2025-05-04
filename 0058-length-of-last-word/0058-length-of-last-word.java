// class Solution {
//     public int lengthOfLastWord(String s) {
//         s = s.trim();
//         String[] words = s.split(" +");
//         return words[words.length - 1].length();
//     }
// }

class Solution {
    public int lengthOfLastWord(String s) {
        int count = 0;
        for(int i=s.length()-1;i>=0;i--){
            if(s.charAt(i) == ' '){
                if(count != 0){return count;}
            }
            else { count++;}
        }
        return count;
    }
}