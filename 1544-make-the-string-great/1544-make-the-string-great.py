class Solution:
    def makeGood(self, s: str) -> str:
        # if len(s) == 1: return s
        # for i in range(len(s) - 1):
        #     if abs(ord(s[i]) - ord(s[i+1])) == 32:
        #         return self.makeGood(s[:i] + s[i+2:])
        # return s
        stack = []
        for char in list(s):
            if stack and abs(ord(char) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)