class Solution:
    def minTimeToType(self, word: str) -> int:
        res = len(word)
        curr = 'a'
        for ch in word:
            mn = min(26 - (abs(ord(ch) - ord(curr))), (abs(ord(ch) - ord(curr))))
            res+=mn
            curr = ch
        return res