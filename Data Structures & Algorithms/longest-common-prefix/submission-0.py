class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            # Compare all the leters at index 1 then compare all letters at 2
            result = ""
            
            for i in range(len(strs[0])): # This is the first index 
            # it doesn't matter the length of this string because the 
            # common prefix will end when any one of the words ends
                for s in strs: # while pointer is at index 1, we look through all words there
                    if i == len(s) or s[i] != strs[0][i]:
                        return result
                result += strs[0][i] 
            return result