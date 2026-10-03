class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, n in enumerate(nums):
            secondNumber = target - n

            if secondNumber in hashMap:
                return [hashMap[secondNumber], i]
            hashMap[n] = i


