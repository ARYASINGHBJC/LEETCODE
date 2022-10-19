class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Ex: words = ["i","love","leetcode","i","love","coding"], k = 2
        c = Counter(words) #c = {'i': 2, 'love': 2, 'leetcode': 1, 'coding': 1}
        
        ans = sorted(c, key = lambda x: (-c[x],x))  #       ans = ['i', 'love', 'coding', 'leetcode']
        #  sort keys are [(-2,'i'), (-2,'love'), (-1,'coding'), (-1,'leetcode')]
        return ans[:k]