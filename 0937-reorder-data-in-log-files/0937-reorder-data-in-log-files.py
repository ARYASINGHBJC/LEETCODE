class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def sort(log):
            a, b = log.split(" ", 1)
            if b[0].isalpha():
                return (0, b, a)
            else:
                return (1,)
        
        return sorted(logs, key = sort)
        # letter = []
        # digit = []
        # for log in logs:
        #     if log.split()[1].isalpha():
        #         letter.append(log)
        #     else:
        #         digit.append(log)
        # return sorted(letter, key = lambda x : (x.split(" ", 1)[1], x.split(" ", 1)[0]))+ digit