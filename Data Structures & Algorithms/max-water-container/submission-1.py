class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxV = 0
        tmpV = 0
        l = 0;
        r = len(heights) - 1

        while r > l:
            tmpV = (r-l) * min(heights[r], heights[l])
            if(tmpV > maxV):
                maxV = tmpV
            if (heights[r] < heights[l]):
                r -= 1
            else:
                l += 1
        
        return maxV





        