class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minNum = min(nums)
        maxNum = max(nums)
        while minNum !=0:
            maxNum , minNum = minNum , maxNum%minNum
        return maxNum

        