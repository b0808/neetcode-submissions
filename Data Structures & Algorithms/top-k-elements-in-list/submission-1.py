class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1+ count.get(num,0)
        print(count)
        arr = []
        for num, frq in count.items():
            arr .append([frq,num])
        print(arr)

        arr.sort()

        res = []

        for i in range(k):
            res.append(arr.pop()[1])
        return res



        