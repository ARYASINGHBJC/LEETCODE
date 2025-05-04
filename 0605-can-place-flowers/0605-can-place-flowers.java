class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int curr = 1;
        int total = 0;
        for(int bed: flowerbed){
            if(bed == 0){
                curr++;
            }else{
                total += (curr - 1)/2;
                curr= 0;
            }
        }
        if (curr != 0){
            total += curr / 2;
        }
        return total >= n;
    }
}