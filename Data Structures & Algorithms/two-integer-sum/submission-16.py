class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k_set ={}
        for i,k in enumerate(nums):
                value = target - k
                if value in k_set:
                    return [k_set[value],i]
                else:
                    k_set[k] = i
                

                







        # b = 0
        # for i,k in enumerate(nums):
        #     m = target - k
        #     if m in nums[i+1:]:
        #         print(m)
        #         b = i

        # for i,m in enumerate(nums):
        #     if nums[i] == target-nums[b] and i!=b:
        #         return [b,i] 


