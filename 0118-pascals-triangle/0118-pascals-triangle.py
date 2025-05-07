class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l = []
        for i in range(numRows):
            temp = []
            for j in range(i+1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append(l[i-1][j-1] + l[i-1][j])
            l.append(temp)
        return l