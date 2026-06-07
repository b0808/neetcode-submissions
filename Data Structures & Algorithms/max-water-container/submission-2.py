class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxq = 0

        start = 0
        end = len(heights)-1

        while start<end:
            diff = end - start
            h = min(heights[end],heights[start])
            maxq = max(h*diff,maxq)



            if heights[start]<=heights[end]:
                start +=1
            else:
                end-=1
        return maxq

        
             
