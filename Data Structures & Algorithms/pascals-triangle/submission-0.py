class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]

        for i in range(numRows - 1):
            temp = [0] + output[-1] + [0]
            newRow = []
            for j in range(len(output[-1]) + 1):
                newRow.append(temp[j] + temp[j + 1])
            output.append(newRow)
        return output
