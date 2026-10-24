class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for i in range(len(words)): # i is a word
            for j in range(len(words)):
                if i == j: # comparing the same word to itself
                    continue 
                if words[i] in words[j]:
                    result.append(words[i])
                    break
        return result
