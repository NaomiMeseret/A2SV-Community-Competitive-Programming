class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        inc = deque()
        dec = deque()
        l = 0
        res = 0
        for r in range(len(nums)):
            while dec and dec[-1] < nums[r]:
                dec.pop()
            dec.append(nums[r])
            while inc and inc[-1] > nums[r]:
                inc.pop()
            inc.append(nums[r])
            while dec[0]-inc[0] > limit:
                value = nums[l]
                if dec[0] == value:
                    dec.popleft()
                if inc[0] == value:
                    inc.popleft()
                l += 1
            res = max(res,r-l+1)
        return res






        