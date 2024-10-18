class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len=0
        l=0
        zero_counts=0
        for r in range(len(nums)):
            if nums[r]==0:
                zero_counts+=1
            while zero_counts>k:
                if nums[l]==0:
                    zero_counts-=1
                l+=1
            max_len=max(max_len,r-l+1)
        return max_len

        

        