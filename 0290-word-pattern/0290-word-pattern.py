# class Solution:
#     def wordPattern(self, pattern: str, str: str) -> bool:
#         # dictionary approach 
#         # Time complexity: O(n)
#         # Space complexity: O(n)
        
#         words = str.split(" ")
#         if not len(words) == len(pattern):
#             return False
        
#         mapping = dict() # key is the pattern, value is the word
        
#         for i in range(len(words)):
#             if pattern[i] not in mapping:
#                 # values() is a set - fast membership testing - O(1) amortised search
#                 if words[i] not in mapping.values(): 
#                     mapping[pattern[i]] = words[i]
#                 else:
#                     return False
#             else:
#                 if not mapping[pattern[i]] == words[i]:
#                     return False
#         return True
class Solution():
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words_list = s.split(" ")
        if len(pattern) != len(words_list):
            return False 
        
        pattern_map = {}
        for p, word in zip(pattern, words_list):
            if p not in pattern_map:
                if word in pattern_map.values():
                    return False
                pattern_map[p] = word 
            else:
                if pattern_map[p] != word:
                    return False
                
                
        return True