class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])): # iterate through indexes
            for s in strs: # iterate through strings
                if i == len(s) or s[i] != strs[0][i]: # I am not sure about this last part       
                    return s[:i]
        return strs[0]
        
