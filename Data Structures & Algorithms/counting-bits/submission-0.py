class Solution:
    def countBits(self, n: int) -> List[int]:
        out = [0] * (n + 1)
        for i in range(n + 1):
            out[i] = i.bit_count()
        return out