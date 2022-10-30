class Solution:
    def digitSum(self, n):
        sm = 0
        while n != 0:
            sm += n % 10
            n //= 10
        return sm
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        lst = 1 # the number of zeros we want to leave at the end
        add = 0
        #if the sum of digits is greater than target, it is most optimal to make the last few digits equal to zero
        while self.digitSum(n + add) > target:
            x = 10 ** lst
            add = x - n % x
            lst += 1
        
        return add