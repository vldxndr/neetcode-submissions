class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        v = []
        nr = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if (nums[i] + nums[j] + nums[k] == 0):
                        triplet = sorted([nums[i], nums[j], nums[k]])
                        if triplet not in v:
                            v.append(triplet)
        return v

        