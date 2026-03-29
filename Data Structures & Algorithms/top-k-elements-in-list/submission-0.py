from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Count how many times each number appears
        count = Counter(nums)

        # Sort numbers by frequency (highest first) and take top k
        return [num for num, freq in count.most_common(k)]
