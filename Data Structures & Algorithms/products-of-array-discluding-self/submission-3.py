class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        forward = [1]*(l)
        p = 1
        for i in range(l):
            forward[i]=p
            p = p*nums[i]
        p = 1
        for i in range(l):
            forward[l-i-1]*=p
            p = p*nums[l-i-1]


        return forward