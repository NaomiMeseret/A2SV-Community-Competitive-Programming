class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        concatenation=0
        while left<right:
            newNum=str(nums[left]) + str(nums[right])
            concatenation+=int(newNum)
            left+=1
            right-=1
        if left==right:
            concatenation+=nums[left]
        return concatenation
        