class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        length = len(nums)
        k = length
        for i in range(length):
            k = k^nums[i]^i
        
        return k

        