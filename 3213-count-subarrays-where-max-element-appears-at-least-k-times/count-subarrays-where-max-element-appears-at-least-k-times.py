class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxElement=max(nums)
        l=0
        countMax=0
        count=0
        for r in range(len(nums)):
            if nums[r]==maxElement:
                countMax+=1
                while countMax >= k: 
                    count += len(nums) - r  
                    if nums[l] == maxElement:
                        countMax -= 1  
                    l += 1
        return count


        