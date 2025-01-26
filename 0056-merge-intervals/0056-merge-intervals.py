class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key = lambda x: x[0])
        start = intervals[0][0]
        end = intervals[0][1]
        for interval in intervals[1:]:
            if end >= interval[0]:
                end = max(end, interval[1])    
            else:
                res.append([start, end])
                start = interval[0]
                end = interval[1]
        res.append([start,end])
        return res