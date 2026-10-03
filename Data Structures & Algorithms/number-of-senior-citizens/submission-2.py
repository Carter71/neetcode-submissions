class Solution:
    def countSeniors(self, details: List[str]) -> int:
        total = 0
        for i in details:
            if int(i[11] + i[12]) > 60:
                total += 1
        return total