class Solution:
    def maximum69Number (self, num: int) -> int:
        s = list(str(num))
        for i, ele in enumerate(s):
            if ele == '6':
                s[i] = '9'
                break
        return int("".join(s))