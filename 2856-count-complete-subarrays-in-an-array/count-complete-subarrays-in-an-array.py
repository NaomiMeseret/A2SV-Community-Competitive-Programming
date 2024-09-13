class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        unique = len(set(nums))
        count = 0
        left = 0
        n = len(nums)

        for right in range(n):
            window = set()
            for i in range(right, n):
                window.add(nums[i])
                if len(window) == unique:
                    count += n - i
                    break
                    
        return count
            