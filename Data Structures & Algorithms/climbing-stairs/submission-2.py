class Solution:

    def fuct(self,n):
        if n==1:
            self.dp[n]=1
            return 1
        if n==0:
            self.dp[n]=1
            return 1
        if self.dp[n]!=-1:
            return self.dp[n]

        self.dp[n] = self.fuct(n-1)+self.fuct(n-2)
        return self.dp[n]

    def climbStairs(self, n: int) -> int:

        self.dp = [-1]*(n+1)

        

        self.fuct(n)
        print(self.dp)

        return self.dp[n]


        