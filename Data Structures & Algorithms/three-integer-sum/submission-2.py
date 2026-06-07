class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        k = []
        n = len(nums)
        # -4 -1 -1
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start = i+1
            end = n-1

            while end>start:
                sum = nums[i]+nums[start]+nums[end]
                if sum==0:
                    k.append([nums[i],nums[start],nums[end]])
                    while start < end and nums[start] == nums[start+1]:
                        start += 1
                    while start < end and nums[end] == nums[end-1]:
                        end -= 1
                    start+=1
                    end -=1
                elif sum>0:
                    end -=1
                elif sum<0:
                    start+=1
                    
        return k

        