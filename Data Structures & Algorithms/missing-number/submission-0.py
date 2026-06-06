class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        length = len(nums)
        k = 0
        for i in range(length):
            k = k^nums[i]^i
        
        return k^length

        