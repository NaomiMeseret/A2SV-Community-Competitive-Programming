class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxLength=0
        nums_zeros=0
        l=0
        for r in range(len(nums)):
            if nums[r]==0:
                nums_zeros+=1
            while nums_zeros > 1:
                if nums[l]==0:
                    nums_zeros-=1
                l+=1
            maxLength=max(maxLength,r-l)
        return maxLength

        