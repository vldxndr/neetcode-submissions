class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seto = set()
        for n in nums:
            if n not in seto:
                seto.add(n)
            else:
                return True
        return False
