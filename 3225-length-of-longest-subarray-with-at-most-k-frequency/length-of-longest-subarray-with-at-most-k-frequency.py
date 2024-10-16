class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        maxLength=0
        seen={}
        l=0
        for r in range(len(nums)):
            seen[nums[r]] =seen.get(nums[r],0)+1
            while seen[nums[r]]>k:
                seen[nums[l]]-=1
                if seen[nums[l]]==0:
                    del seen[nums[l]]
                l+=1
            maxLength=max(maxLength,r-l+1)
        return maxLength


        