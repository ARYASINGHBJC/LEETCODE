class Solution:
    def maxDifference(self, s: str) -> int:
        ele = set(s)
        oddFreq = 0
        evenFreq = float('inf')
        for e in ele:
            if s.count(e) % 2 == 0:
                evenFreq = min(evenFreq, s.count(e))
            else:
                oddFreq = max(oddFreq, s.count(e))
        if not oddFreq or not evenFreq:
            return 0
        return oddFreq - evenFreq