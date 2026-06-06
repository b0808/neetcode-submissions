class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix),len(matrix[0])
        nums = matrix
        lowm,highm,lown,highn = 0,m-1,0,n-1
        print(nums[0][0])
        while highm>=lowm:
            mid = int((highm+lowm)/2)
            if target<=nums[mid][n-1] and target >= nums[mid][0]:
                break
            if target>nums[mid][n-1]:
                lowm = mid+1
            if target<nums[mid][n-1]:
                highm = mid-1

        while highn>=lown:
            midn = int((highn+lown)/2)
            if target==nums[mid][midn]:
                return True
            if target>nums[mid][midn]:
                lown = midn+1
            if target<nums[mid][midn]:
                highn = midn-1
        
        return False




        