class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0]*(n+1)
        for i in range(n): 
            dp[i+1] = max(dp[i+1] , dp[i])
            points , brain = questions[i]
            target = i+brain+1
            if target>n:
                target = n
            dp[target] = max(dp[target] , dp[i]+points)
        return dp[n]

        