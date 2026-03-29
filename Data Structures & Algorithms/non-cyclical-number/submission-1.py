class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n not in seen:
            seen.add(n)
            n = self.fc(n)

            if n == 1:
                return True
        
        return False
    

    def fc (self, n : int) -> int:
        out = 0
        while n:
            dig = n % 10
            out += dig * dig
            n = n // 10
        return out
                