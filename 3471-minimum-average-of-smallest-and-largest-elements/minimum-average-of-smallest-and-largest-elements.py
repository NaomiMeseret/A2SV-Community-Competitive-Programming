class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages=[]
        nums.sort()
        left=0
        right=len(nums)-1
        for i in range(len(nums)//2):
            averages.append((nums[left]+nums[right])/2)
            left+=1
            right-=1
        return min(averages)
        