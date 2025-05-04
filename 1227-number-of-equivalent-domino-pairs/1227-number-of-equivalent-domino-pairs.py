class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        hp = defaultdict(int)
        for domino in dominoes:
            key = tuple(sorted(domino))
            hp[key] += 1
        c = 0
        for val in hp.values():
            s = val*(val-1)//2
            c += s
        return c
        # cnt = 0
        # for i in range(len(dominoes)):
        #     for j in range(i+1, len(dominoes)):
        #         if dominoes[i][0] == dominoes[j][0] and dominoes[i][1] == dominoes[j][1] or dominoes[i][0] == dominoes[j][1] and dominoes[j][0] ==  dominoes[i][1]:
        #             cnt += 1
        # return cnt
