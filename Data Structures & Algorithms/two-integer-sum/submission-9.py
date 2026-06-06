class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        b = 0
        for i,k in enumerate(nums):
            m = target - k
            if m in nums[i+1:]:
                print(m)
                b = i

        for i,m in enumerate(nums):
            if nums[i] == target-nums[b] and i!=b:
                return [b,i] 


