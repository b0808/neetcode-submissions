class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        for num in nums:
            count[num] = 1+count.get(num,0)
        print(count)
        count = sorted(count.items(), key=lambda x: x[1], reverse=True)

        i = 0 
        for key,item in count:
            i=i+1
            if k>=i:
                res.append(key)
        return res



        