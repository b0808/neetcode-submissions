class Solution:

    # def fuct(self,n):
    #     if n==1:
    #         self.dp[n]=1
    #         return 1
    #     if n==0:
    #         self.dp[n]=1
    #         return 1
    #     if self.dp[n]!=-1:
    #         return self.dp[n]
    #     self.dp[n] = self.fuct(n-1)+self.fuct(n-2)
    #     return self.dp[n]


    # def climbStairs(self, n: int) -> int:
    #     self.dp = [-1]*(n+1)
    #     self.fuct(n)
    #     print(self.dp)
    #     return self.dp[n]

    def climbStairs(self, n: int) -> int:

        dp = [-1]*(n+1)

        for i in range(n+1):
            if i==0 or i==1:
                dp[i]=1
            else:
                dp[i] = dp[i-1]+dp[i-2]
        print(dp)
        return dp[n]


        