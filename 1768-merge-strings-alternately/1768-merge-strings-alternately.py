class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge = ""
        m = len(word1)
        n = len(word2)
        i = 0
        j = 0
        while i < m or j < n:
            if i < m:
                merge += word1[i]
                i += 1
            if j < n:
                merge += word2[j]
                j += 1
        return merge
        