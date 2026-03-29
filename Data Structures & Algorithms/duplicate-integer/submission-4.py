class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        bam = set()
        for n in nums:
            if n not in bam:
                bam.add(n)
            else:
                return True

        return False        