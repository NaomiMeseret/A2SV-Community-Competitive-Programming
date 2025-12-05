class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        if (sum(nums)&1)==0:
            return len(nums)-1 
        else:
            return 0
        