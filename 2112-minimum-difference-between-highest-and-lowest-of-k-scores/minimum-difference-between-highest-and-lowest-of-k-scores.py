class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        mindiff=float("inf")
        if k==1:
            return 0
        for i in range(len(nums)-k+1):
            current_diff=nums[i+k-1]-nums[i]
            mindiff=min(mindiff,current_diff)
        return mindiff



        