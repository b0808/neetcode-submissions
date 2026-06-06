class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minv = prices[0]
        maxv = 0

        for s in prices:
            maxv = max(maxv,s-minv)
            minv = min(s,minv)
        return maxv

        