import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = []
        kth = []
        for i,j in points:
            dis.append([(i*i+j*j),i,j])
        heapq.heapify(dis)
        for m in range(k):
            item,i,j = heapq.heappop(dis)
            kth.append([i,j])

        return kth



        


        