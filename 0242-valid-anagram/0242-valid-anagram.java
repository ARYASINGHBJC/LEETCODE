class Solution {
    public boolean isAnagram(String s, String t) {     
        int temp[] = new int[26];
        if(s.length()!= t.length()){
            return false;
        } 
        for (char cr: s.toCharArray()){
            temp[cr - 'a']++;
        }   
        for(char cr: t.toCharArray()){
            if(temp[cr - 'a'] == 0){
                return false;
            }temp[cr - 'a']--;
        }
        return true;
        // if(s.length() != t.length()){
        //     return false;
        // }
        // HashMap<Character, Integer> seen = new HashMap<>();
        // for(int i = 0; i < s.length();i++){
        //     char currChar = s.charAt(i);
        //     seen.put(currChar, seen.getOrDefault(currChar, 0) + 1);
        // }
        // for(int i = 0; i<t.length();i++){
        //     char currChar = t.charAt(i);
        //     if(!seen.containsKey(currChar) || seen.get(currChar) == 0){
        //         return false;
        //     }
        //     else{
        //         seen.put(currChar, seen.get(currChar) - 1);
        //     }
        // }
        // return true;
    }
}