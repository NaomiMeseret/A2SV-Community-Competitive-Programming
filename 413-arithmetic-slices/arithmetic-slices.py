class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        count=0
        l=0
        if len(nums)<3:
            return 0
        for i in range(1, len(nums) - 1):
            if nums[i] - nums[i - 1] == nums[i + 1] - nums[i]:
                l += 1
                count += l
            else:
                l = 0
        return count
        
        