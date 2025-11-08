class Solution(object):
    def majorityElement(self, nums):
        counts = Counter(nums)
        for num in nums:
            if counts[num] > len(nums) // 2:
                return num
        