class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        res = 0;
        for num in s:
            counter = 1
            if num - 1 in s:
                continue
            else:
                while num + 1 in s:
                    counter += 1
                    num = num + 1
            res = max(counter, res)

        return res
            
