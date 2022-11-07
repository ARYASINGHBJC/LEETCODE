class Solution:
    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace('6', '9', 1))
        # s = list(str(num))
        # for i, ele in enumerate(s):
        #     if ele == '6':
        #         s[i] = '9'
        #         break
        # return int("".join(s))