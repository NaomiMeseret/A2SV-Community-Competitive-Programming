class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(x):
            if x == 0:
                return 0
            if x<0:
                return float("inf")
            if x in memo:
                return memo[x]
            ans = float("inf")
            for c in coins:
                ans = min(ans , 1+dp(x-c))
            memo[x] =ans
            return ans
        res = dp(amount)
        return res if res!=float("inf") else -1
        