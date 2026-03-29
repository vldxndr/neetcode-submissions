class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sD = {}
        tD = {}

        if len(s) != len(t):
            return False

        for c1, c2 in zip(s, t):
            if c1 not in sD:
                sD[c1] = 1
            else:
                sD[c1] += 1
            if c2 not in tD:
                tD[c2] = 1
            else:
                tD[c2] += 1
        return sD == tD
        