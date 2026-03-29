from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Frecv = {}
        resList = []

        for n in nums:
            if n not in Frecv:
                Frecv[n] = 1
            else:
                Frecv[n] += 1

        sorted_keys = sorted(Frecv.keys(), key=Frecv.get, reverse=True)
        return sorted_keys[:k]

        