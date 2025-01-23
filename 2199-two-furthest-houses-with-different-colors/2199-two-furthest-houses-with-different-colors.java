class Solution {
    public int maxDistance(int[] colors) {
        int maxDistance = 0;
        for(int i = 0; i <colors.length; i++){
            if(colors[0] != colors[i]){
                maxDistance = Math.max(maxDistance, i);
            }
            if(colors[colors.length - 1] != colors[i]){
                maxDistance = Math.max(maxDistance, colors.length - i - 1);
            }
        }
        return maxDistance;
    }
}