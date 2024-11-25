class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count_nums=Counter(nums)
        for num in nums:
            if count_nums[num]>1:
                return True
        return False
        