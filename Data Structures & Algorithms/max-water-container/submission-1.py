class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max = 0

        start = 0
        end = len(heights)-1

        while start<end:
            diff = end - start
            h = min(heights[end],heights[start])
            curr = h*diff

            if max<curr:
                max = curr


            if heights[start]<=heights[end]:
                start +=1
            else:
                end-=1
        return max

        
             
