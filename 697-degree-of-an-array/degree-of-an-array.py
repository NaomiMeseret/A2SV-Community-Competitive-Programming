class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first = {}
        last = {}
        count = {}
        for i in range(len(nums)):
            num = nums[i]
            if num not in first :
                first[num] = i
            last[num] = i
            if num in count:
                count[num] +=1
            else:
                count[num] = 1
        degree = max(count.values())
        minlength = len(nums)
        for num in count:
            if count[num] == degree:
                length = last[num] - first[num] +1
                if length < minlength:
                    minlength  = length
        return minlength
        