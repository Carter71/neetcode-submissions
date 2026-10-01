class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # base case is always -1
        # reverse through the list but return in proper order
        # the new max is the highest between the old max and the current number
            # new max = max(oldmax, arr[i])

        baseCase = -1 # Last number should always be -1
# [1, 2, 3, 4, 5] [0, 4]
        for i in range(len(arr) - 1, -1, -1): # iterate over the list starting at 
            newMax = max(baseCase, arr[i])
            arr[i] = baseCase
            baseCase = newMax
        return arr


        
        