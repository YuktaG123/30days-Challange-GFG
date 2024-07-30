class Solution:
    def countMin(self, s):
        # code here
        n=len(s)
        dp=[[0]*(n) for i in range(n)]
        for i in range(n-1):
            if s[i]!=s[i+1]:
                dp[i][i+1]=1
        for i in range(n-1,-1,-1):
            for j in range(i+2,n):
                if s[i]!=s[j]:
                    dp[i][j]=min(1+dp[i+1][j],1+dp[i][j-1])
                else:
                    dp[i][j]=min(1+dp[i+1][j],1+dp[i][j-1],dp[i+1][j-1])
        return dp[0][n-1]


