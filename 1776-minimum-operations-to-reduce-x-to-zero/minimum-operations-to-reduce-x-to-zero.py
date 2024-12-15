class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total_sum = sum(nums)
        target = total_sum - x
        if target < 0:
            return -1
        
        l = 0
        current_sum = 0
        max_len = -1
        
        for r in range(len(nums)):
            current_sum += nums[r]
            
            while current_sum > target:
                current_sum -= nums[l]
                l += 1
            
            if current_sum == target:
                max_len = max(max_len, r - l + 1)
        
        return len(nums) - max_len if max_len != -1 else -1
            