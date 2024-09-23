class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
        count=0
        for left in range(len(nums)):
            for right in range(1,len(nums)):
                if (nums[left]+nums[right]<target) and (left<right):
                    count+=1
        return count

        