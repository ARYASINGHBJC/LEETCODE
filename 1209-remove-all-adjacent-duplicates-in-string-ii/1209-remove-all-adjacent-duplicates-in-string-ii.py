class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] #(character, frequency)
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])
            if stack[-1][1] == k:
                stack.pop()
        return "".join(key*value for key, value in stack)