class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        print(numbers)
        l = len(numbers)
        m = 0 
        n = len(numbers)-1
        while m<n:
            # print(m,n,"start")
            l = numbers[m]+numbers[n]
            if l == target:
                return [m+1,n+1]
            if l<target:
                m = m+1
            else:
                n = n-1

