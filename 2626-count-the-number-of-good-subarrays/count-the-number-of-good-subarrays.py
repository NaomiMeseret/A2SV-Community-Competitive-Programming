class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        c = defaultdict(int)
        res = 0
        l = 0
        pairs = 0
        for r in range(len(nums)):
            pairs += c[nums[r]]
            c[nums[r]] += 1
            while pairs - (c[nums[l]] - 1) >= k:
                pairs -= c[nums[l]] - 1
                c[nums[l]] -= 1
                l += 1
            if pairs >= k:
                res += l + 1
        return res