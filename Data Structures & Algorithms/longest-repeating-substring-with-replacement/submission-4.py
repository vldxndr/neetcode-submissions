class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        hm = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            hm[s[r]] = 1 + hm.get(s[r], 0)
            maxf = max(maxf, hm[s[r]])

            if k < r - l + 1 - maxf:
                
                hm[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return res

