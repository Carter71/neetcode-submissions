class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashs, hasht = {}, {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            hashs[s[i]] = 1 + hashs.get(s[i], 0) # the get allow us to that 
            hasht[t[i]] = 1 + hasht.get(t[i], 0) # same value as the variable
        for c in hashs:
            if hashs[c] != hasht.get(c, 0):
                return False
        return True
        # The goal is to iterate through each word and record the counts of each letter in a separt dictionary, then compare each key value pair to the other dictionary