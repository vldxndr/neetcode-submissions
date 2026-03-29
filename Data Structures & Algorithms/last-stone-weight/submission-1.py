class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 2:
            stones.sort()
            first = stones.pop()
            second = stones.pop()
            if second == first:
                continue
            else:
                stones.append(abs(first - second))
        if len(stones) == 2:
            return abs(stones[1] - stones[0])
        else:
            return stones[0]