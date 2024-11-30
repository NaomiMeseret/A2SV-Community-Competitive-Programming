class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=0
        maxLen=0
        zeroCount=0
        for r in range(len(nums)):
            if nums[r]==0:
                zeroCount+=1
            while zeroCount>1:
                if nums[l]==0:
                    zeroCount-=1
                l+=1
            maxLen=max(maxLen,r-l)
        return maxLen
        
        