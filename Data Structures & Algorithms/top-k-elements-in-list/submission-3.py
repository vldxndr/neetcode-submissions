from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tally = Counter(nums)

        top_pairs = tally.most_common(k)

        top_keys = [item[0] for item in top_pairs]

        return top_keys
        