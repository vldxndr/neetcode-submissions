class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for n in nums:
            hm[n] = hm.get(n, 0) + 1
        
        sorted_items = sorted(hm.items(), key=lambda item: item[1],     reverse=True)

        res = []
        # 2. Grab the keys (the numbers) for the top k items
        for i in range(k):
            res.append(sorted_items[i][0])
            
        return res


