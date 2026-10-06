class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        highest = 0
        # Have two variables
        # One is the current count and one is the highest number seen "or highest consecutive"
        # For each number in nums see if it's a 1 or 0
        # If it's 1, add it to the count
        # This should continue repeating and adding to the count, until we hit a 0
        # Count should become highest 
        # count should go back to 0 and repeate the process
        # 
        
        
        for i in nums:
            if i == 1:
                count += 1
            else: # When i is 0
                if count > highest:
                    highest = count # records the highest
                count = 0
            if count > highest:
                highest = count
        return highest