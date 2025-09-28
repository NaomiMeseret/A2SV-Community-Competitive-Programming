class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        def dp(i):
            if i <= 1 :
                return 0 
            if i in memo :
                return memo[i]
            oneStep = dp(i-1) + cost[i-1]
            twoSteps = dp(i-2)  + cost[i-2]
            memo[i] = min(oneStep , twoSteps)
            return memo[i]
        return dp(n)
        