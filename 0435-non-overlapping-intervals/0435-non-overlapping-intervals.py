class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1])
        cnt = 0
        first = intervals[0][1]
        for interval in intervals[1:]:
            if first > interval[0]:
                cnt += 1
            else:
                first = interval[1]
        return cnt