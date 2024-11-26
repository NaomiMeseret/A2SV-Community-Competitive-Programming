class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        leftSum=0
        totalSum=sum(nums)
        for i,num in enumerate(nums):
            rightSum=totalSum-leftSum-num
            if rightSum==leftSum:
                return i
            leftSum+=num
        return -1

        