class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        dp = {}
        maxLen = float("-inf")
        for num in arr:
            dp[num] = dp.get(num-difference , 0)+1
            maxLen = max(maxLen ,dp[num])
        return maxLen


        