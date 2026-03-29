class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}

        for i, n in enumerate(nums):
            need = target - n

            if need in maps:
                return [maps[need], i]
            maps[n] = i