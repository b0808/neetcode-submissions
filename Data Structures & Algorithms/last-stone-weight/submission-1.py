import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        print(stones)
        if len(stones)==1:
            return abs(stones[0])

        while len(stones)>1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second-first!=0:
                heapq.heappush(stones,first-second)
            heapq.heapify(stones)
        if len(stones)==1:
            return abs(stones[0])
        else:
            return 0

        