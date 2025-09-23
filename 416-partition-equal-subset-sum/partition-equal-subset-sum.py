class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s =sum(nums)
        if s%2 !=0:
            return False
        target = s//2
        memo = {}
        def dp(i,t):
            if t == 0:
                return True
            if i>=len(nums) or t<0:
                return False 
            if (i,t) in memo:
                return memo[(i,t)]
            memo[(i,t)] = dp(i+1,t-nums[i]) or dp(i+1,t)
            return memo[(i,t)]
        return dp(0,target)
        