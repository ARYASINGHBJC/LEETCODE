class Solution(object):
    def groupAnagrams(self, strs):
        l = {}
        for ele in strs:
            sortedEle = "".join(sorted(ele))
            if sortedEle not in l:
                l[sortedEle] = [ele]
            else:
                l[sortedEle].append(ele)
        return l.values()
        