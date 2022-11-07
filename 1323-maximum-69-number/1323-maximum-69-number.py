class Solution:
    def maximum69Number (self, num: int) -> int:
        n = num
        for i in reversed(range(4)):
            d, n = divmod(n , 10**i)
            if d == 6:
                return num + 3*10**i
        return num
        # return int(str(num).replace('6', '9', 1))
        # s = list(str(num))
        # for i, ele in enumerate(s):
        #     if ele == '6':
        #         s[i] = '9'
        #         break
        # return int("".join(s))