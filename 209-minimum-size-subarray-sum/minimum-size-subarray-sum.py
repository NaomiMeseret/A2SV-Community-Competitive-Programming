class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        minLength  = float("inf")
        totalSum = 0
        for r in range(len(nums)):
            totalSum += nums[r]
            while totalSum>= target:
                minLength = min(minLength , r-l+1)
                totalSum -=nums[l]
                l+=1
        if minLength != float("inf"):
            return minLength
        else:
            return 0



    

       

        