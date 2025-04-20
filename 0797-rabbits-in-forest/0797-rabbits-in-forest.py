from collections import Counter
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
      c = Counter(answers)
      tl = 0
      for rb in c:
        tl += ceil(c[rb]/(rb+1))*(rb+1)
      return tl