class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        k = 1
        l  = len(nums)
        m = [1]*l
        n = [1]*l
        
        



        first = 1
        second  = 1
        for i in range(l-1):
            first = first*nums[i]
            m[i+1] = first

        
        for i in range(l-1):
            second= second*nums[l-1-i]
            n[l-i-2] = second
        f = []
        for i in range(l):
            f.append(m[i]*n[i])
        
        return f






        