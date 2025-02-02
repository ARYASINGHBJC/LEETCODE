class Solution {
    public int maxDifference(String s) {
        HashMap<Character, Integer> ele = new HashMap<>();
        for (char c : s.toCharArray()) {
            ele.put(c, ele.getOrDefault(c, 0) + 1);
        }
        int oddFreq = 0;
        int evenFreq = Integer.MAX_VALUE;
        for(char e: ele.keySet()){
            if(ele.get(e) % 2 == 0){
                evenFreq = Math.min(evenFreq, ele.get(e));
            }else{
                oddFreq = Math.max(oddFreq, ele.get(e));
            }
        }
        return oddFreq - evenFreq;
    }
}