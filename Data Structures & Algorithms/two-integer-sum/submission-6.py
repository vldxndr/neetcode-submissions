class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i in range(len(nums)):
            want = target - nums[i]

            if want in hm:
                return [hm[want], i]
            else:
                hm[nums[i]] = i
        