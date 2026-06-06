class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums)==1:
            return nums[0]


        pp=nums[0]
        p=max(nums[0],nums[1])

        for i in range(2,len(nums)):
            curr = max(p,pp+nums[i])
            pp=p
            p=curr
        
        return p
        