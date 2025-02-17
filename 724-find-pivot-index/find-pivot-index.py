class Solution(object):
    def pivotIndex(self, nums):
        # sumLeft = 0
        # sumRight = sum(nums[1:])
        # if sumLeft == sumRight:
        #     return 0
        # for i in range(1, len(nums)):
        #     sumLeft += nums[i-1]
        #     sumRight -= nums[i]
        #     if sumLeft == sumRight:
        #         return i

        # return -1
        acc=0
        for i in range(len(nums)):
            acc+=nums[i]
            nums[i]=acc
        if nums[-1]-nums[0]==0:
            return 0
        for i in range(1,len(nums)):
            l=nums[i-1]
            r=nums[-1]-nums[i]
            if l==r:
                return i
        return -1

            