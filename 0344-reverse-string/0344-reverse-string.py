class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead
        """
        # i = 0
        # j = len(s) -1
        # mid = (i+j)//2 +1
        # while i < mid:
        #     s[i],s[j] = s[j], s[i]
        #     i += 1
        #     j -= 1
        # return s
        def reverse(l, r):
            if l < r:
                s[l], s[r] = s[r], s[l]
                reverse(l+1, r-1)
        reverse(0, len(s)-1)
