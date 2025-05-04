class Solution {
    public String kthDistinct(String[] arr, int k) {
        HashMap<String, Integer>seen = new HashMap<>();
        for(int i = 0;i < arr.length;i++){
            String currChar = arr[i];
            seen.put(currChar, seen.getOrDefault(currChar, 0)+1);
        }
        int cnt = 0;
        for(String word: arr){
            if(seen.containsKey(word) && seen.get(word) == 1){
                cnt +=1;
                if(cnt == k){
                    return word;
                }
            }
        }
        return "";
    }
}