import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower, upper = 1, max(piles)

        res = upper

        while lower <= upper:

            k = (lower + upper) // 2
            hours = 0

            for p in piles:
                hours += math.ceil(p/k)

            if hours <= h:
                res = k
                upper = k - 1
            else:
                lower = k + 1

        return res
                