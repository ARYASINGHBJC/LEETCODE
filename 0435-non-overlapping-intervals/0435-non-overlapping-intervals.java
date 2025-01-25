class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparingInt(a -> a[1]));
        int first= intervals[0][1];
        int cnt = 0;
        for(int i =1; i < intervals.length; i++){
            if(first > intervals[i][0]) cnt++;
            else first = intervals[i][1];
        }
        return cnt;
    }
}