class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} # value : index
        for i, n in enumerate(nums):
            secondNumber = target - n
            if secondNumber in hashMap:
                # return True
                # Need to get the two index of the number
                return [hashMap[secondNumber], i]
            hashMap[n] = i