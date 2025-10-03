class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]*(n+1)
        for i in range(1,n+1):
            count = float("inf")
            j = 1
            while j*j <= i:
                count = min(count , dp[i-j*j]+1)
                j+=1
            dp[i] = count
        return dp[n]
        