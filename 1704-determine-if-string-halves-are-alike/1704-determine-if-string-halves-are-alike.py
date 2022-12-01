class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l = len(s)
        m = l // 2
        a = s[:m]
        b = s[m:]
        cnt1 = 0
        cnt2 = 0
        for ele in a:
            if ele.lower() in 'aeiou':
                cnt1 += 1
        for ele in b:
            if ele.lower() in 'aeiou':
                cnt2 += 1
        return cnt1 == cnt2