class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        
        res = 0
        temp = 1

        for n in num_set:
            if (n - 1) not in num_set:
                temp = 1
                start = n
                while (n + 1) in num_set:
                    temp += 1
                    n += 1
            res = max(res, temp)

        return res


