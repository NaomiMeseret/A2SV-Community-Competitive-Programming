class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        count = {}
        for i, num in enumerate(sorted_nums):
            if num not in count:
                count[num] = i
        result = [count[num] for num in nums]
        
        return result
        

        