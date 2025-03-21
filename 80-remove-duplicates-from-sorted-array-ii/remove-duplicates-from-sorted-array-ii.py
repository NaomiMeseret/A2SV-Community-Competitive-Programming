class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 1
        count = 1
        
        while right < len(nums):
            if nums[left] == nums[right]:
                count += 1
                if count <= 2:
                    left += 1
                    nums[left] = nums[right]
            else:
                count = 1
                left += 1
                nums[left] = nums[right]
            right += 1
        
        return left + 1
        

        