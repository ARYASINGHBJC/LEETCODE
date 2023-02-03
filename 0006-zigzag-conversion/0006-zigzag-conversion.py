# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         if numRows == 1: return s
#         res = ""
#         for r in range(numRows):
#             increment = 2*(numRows-1)
#             for i in range(r, len(s), increment):
#                 res += s[i]
#                 if r > 0 and r < numRows - 1 and i + increment - 2*r < len(s):
#                     res += s[i + increment - 2*r]
#         return res
class Solution(object):
    def convert(self, s, numRows):
        step = (numRows == 1) - 1  # 0 or -1  
        rows, idx = [''] * numRows, 0
        for c in s:
            rows[idx] += c
            if idx == 0 or idx == numRows-1: 
                step = -step  #change direction  
            idx += step
        return ''.join(rows)