class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        min_val = min(nums)
        max_val = max(nums)
        new_min = min_val + k
        new_max = max_val - k
        return max(0, new_max - new_min)

        