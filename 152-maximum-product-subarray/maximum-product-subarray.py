class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_p=nums[0]
        min_p=nums[0]
        result=nums[0]
        for r in range(1,len(nums)):
            if nums[r]<0:
                max_p,min_p=min_p,max_p
            max_p=max(nums[r],max_p*nums[r])
            min_p=min(nums[r],min_p*nums[r])
            result=max(result,max_p)
        return result

        