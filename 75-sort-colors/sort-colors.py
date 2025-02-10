class Solution:
    def sortColors(self, nums: List[int]) -> None:
        maxNum=max(nums)
        count=[0]*(maxNum+1)
        for num in nums:
            count[num]+=1
        target=0
        for index,value in enumerate(count):
            for i in range(value):
                nums[target]=index
                target+=1
        return nums






        