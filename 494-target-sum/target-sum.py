class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def count(index ,currSum):
            if index == len(nums):
                return 1 if currSum == target else 0
            if (index , currSum) in memo:
                return memo[(index , currSum)]
            add = count(index+1 ,currSum+nums[index])
            sub = count(index+1 , currSum-nums[index])
            memo[(index , currSum)] = add+sub
            return memo[(index , currSum)]
        return count(0,0)
        