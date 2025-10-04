class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)
        while l<r:
            mid = (l+r)//2
            count = 1
            curr = 0
            for num in nums:
                if curr+num<=mid:
                    curr +=num
                else:
                    count +=1
                    curr = num
                    if count>k:
                        break
            if count<=k:
                r = mid
            else:
                l = mid+1
        return l
        