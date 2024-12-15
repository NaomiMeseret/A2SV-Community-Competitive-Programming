class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l=0
        p=1
        count=0
        if k<=1:
            return 0
        for r in range(len(nums)):
            p*=nums[r]
            while p>=k:
                p//=nums[l]
                l+=1
            count+=r-l+1
        return count
            
        


        