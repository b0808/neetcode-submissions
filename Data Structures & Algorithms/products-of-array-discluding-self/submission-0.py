class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        forward = [1]*(len(nums))
        bacward = [1]*(len(nums))
        print(forward,bacward)
        p = 1
        for i in range(len(nums)):
            forward[i]=p
            p = p*nums[i]
            print(p,nums)
        p = 1
        for i in range(len(nums)):
            bacward[len(nums)-i-1]=p*forward[len(nums)-i-1]
            p = p*nums[len(nums)-i-1]
        print(forward,bacward)

        return bacward