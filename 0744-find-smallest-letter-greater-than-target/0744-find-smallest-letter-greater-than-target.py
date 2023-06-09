class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for ele in letters:
            if ord(ele) > ord(target):
                return ele
        else:
            return letters[0]