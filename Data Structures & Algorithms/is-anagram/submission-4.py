class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashS = {}
        hashT = {}

        for i in range(len(s)):
            hashS[s[i]] = 1 + hashS.get(s[i], 0)
            hashT[s[i]] = 1 + hashT.get(t[i], 0)
        for c in t:
            if c in hashS and hashS[c] > 0:
                hashS[c] -= 1
            else:
                return False
        return True