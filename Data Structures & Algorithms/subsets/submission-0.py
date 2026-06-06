class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        results = []
        stack = []

        def recc(i,stack):

            if i>= len(nums):
                results.append(stack.copy())
                return
            stack.append(nums[i])
            recc(i+1,stack)
            stack.pop()
            recc(i+1,stack)
        
        recc(0,stack)

        return results
        