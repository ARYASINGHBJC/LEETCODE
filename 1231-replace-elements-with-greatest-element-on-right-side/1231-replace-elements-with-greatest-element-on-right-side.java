class Solution {
    public int[] replaceElements(int[] arr) {
       int res[] = new int[arr.length];
        for(int i =0 ;i < arr.length -1 ;i++){
            int mx = 0;
            for(int j= i+1; j < arr.length; j++){
                mx = Math.max(mx, arr[j]);
                }
            res[i] =  mx;
            }
        res[arr.length-1] = -1; 
        return res;
        }
        
    }