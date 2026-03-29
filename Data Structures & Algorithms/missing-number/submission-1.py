class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        res = (len(nums) * (len(nums) + 1)) // 2

        for i in range(len(nums)):
            res -= nums[i]
        return res