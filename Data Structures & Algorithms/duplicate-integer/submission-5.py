class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sub = set()

        for n in nums:
            if n not in sub:
                sub.add(n)
            else:
                return True
        return False