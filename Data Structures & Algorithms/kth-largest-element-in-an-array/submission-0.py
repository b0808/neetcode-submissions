import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [ -s for s in nums]
        heapq.heapify(nums)
        for i in range(k):
            m = heapq.heappop(nums)

        return -m
        