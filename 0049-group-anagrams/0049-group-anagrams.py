class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = defaultdict(list)
        for i in strs:
            l[''.join(sorted(i))].append(i)
        return l.values()
        # l = {}
        # for ele in strs:
        #     sortedEle = "".join(sorted(ele))
        #     if sortedEle not in l:
        #         l[sortedEle] = [ele]
        #     else:
        #         l[sortedEle].append(ele)
        # return l.values()