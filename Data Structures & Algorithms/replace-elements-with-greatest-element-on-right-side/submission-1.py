class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        highest = -1
        if len(arr) > 1:
            arr.append(highest)
        else:
            return [-1]
        for i in range(len(arr)-1, -1, -1):
            if arr[i] < highest:
                arr[i] = highest
                highest = arr[i]
            else:
                highest = arr[i]
        arr.pop(0)
        return (arr)