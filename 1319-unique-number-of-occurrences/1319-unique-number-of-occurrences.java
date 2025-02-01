class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        HashMap<Integer, Integer> freq = new HashMap<>();
        for(int i= 0; i< arr.length; i++){
            if(freq.containsKey(arr[i])){
                int cnt = freq.get(arr[i]);
                freq.put(arr[i], cnt+1);
            }else{
                freq.put(arr[i], 1);
            }
        }
        HashSet<Integer> count = new HashSet<>();
        for (int occurrence : freq.values()) {
            if (!count.add(occurrence)) {
                return false;
            }
        }
        return true;
    }
}