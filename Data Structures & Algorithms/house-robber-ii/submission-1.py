class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[1],nums[0])
        pp=nums[1]
        p=max(nums[1],nums[2])

        for i in range(3,len(nums)):
            curr = max(p,pp+nums[i])
            pp=p
            p=curr

        p1 = p

        pp=nums[0]
        p=max(nums[1],nums[0])
        for i in range(2,len(nums)-1):
            curr = max(p,pp+nums[i])
            pp=p
            p=curr
        p2 = p
    
        return max(p1,p2) 
        
        
        

        