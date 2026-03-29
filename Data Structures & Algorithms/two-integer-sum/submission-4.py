class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hM = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            
            if needed in hM:
                return [hM[needed], i]
            hM[nums[i]] = i

        