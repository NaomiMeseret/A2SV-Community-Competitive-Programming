class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dp(i):
            if i in memo:
                return memo [i]
            if i >= len(nums):
                return 0
            memo[i] = max(dp(i+1),nums[i]+dp(i+2))
            return memo[i]
        return dp(0)
        