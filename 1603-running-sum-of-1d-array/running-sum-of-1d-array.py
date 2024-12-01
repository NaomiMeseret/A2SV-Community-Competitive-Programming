class Solution(object):
    def runningSum(self, nums):
        start=0
        for i in range(len(nums)):
            start+=nums[i]
            nums[i]=start
        return nums


        
        