class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxV = 0;
        tmpV = 0;
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                tmpV = (j-i) * min(heights[i], heights[j])
                if (tmpV > maxV):
                    maxV = tmpV
        return maxV





        