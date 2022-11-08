class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def generate(left, right, s):
            if len(s) == 2*n:
                res.append(s)
                return
            if left < n:
                generate(left + 1, right, s + "(")
            if right < left:
                generate(left, right+ 1, s + ")")
            
        generate(0, 0, "")
        return res