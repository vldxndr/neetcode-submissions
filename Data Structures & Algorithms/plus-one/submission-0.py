class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ""
        for i in range(len(digits)):
            string += str(digits[i])

        integer = int(string)
        integer += 1
        out = []

        while integer > 0:
            out.append(integer % 10)
            integer = integer // 10

        out.reverse()
        return out

            


