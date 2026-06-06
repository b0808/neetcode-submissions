class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # def uniq(i,j):

        #     if i==0 and j==1:
        #         return 1
        #     if i==1 and j==0:
        #         return 1

        #     if i==0:
        #         return uniq(i,j-1)
        #     if j==0:
        #         return uniq(i-1,j)
         

        #     return uniq(i,j-1)+uniq(i-1,j)
        
        # return uniq(n-1,m-1)
        
        dp = [[1 for i in range(n)] for j in range(m)]

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]

        print(dp)

        return dp[m-1][n-1]
