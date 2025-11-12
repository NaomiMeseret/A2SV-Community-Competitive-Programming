class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        rem = total%p
        if rem == 0 :
            return 0
        prefix = 0
        seen = {0:-1}
        ans = len(nums)
        for i , num in enumerate(nums):
            prefix = (prefix+num)%p
            target = (prefix-rem+p)%p
            if target in seen:
                ans = min(ans , i-seen[target])
            seen[prefix] =  i 
        if ans<len(nums):
            return ans
        else:
            return -1
        