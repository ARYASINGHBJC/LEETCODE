class Solution {
    public boolean isAnagram(String s, String t) {        
        if (s.length() != t.length()) {
            return false; // Anagrams must have the same length
        }

        HashMap<Character,Integer> seen = new HashMap<>();
        for(int i = 0; i<s.length();i++){
            char currChar = s.charAt(i);
            seen.put(currChar, seen.getOrDefault(currChar, 0) +1);
        }
        for(int i = 0; i<t.length();i++){
             char currChar = t.charAt(i);
            if(!seen.containsKey(currChar) || seen.get(currChar) ==0){
                return false;
            }else{
                seen.put(currChar, seen.get(currChar) -1);
            }
        }
        return true;
    }
}