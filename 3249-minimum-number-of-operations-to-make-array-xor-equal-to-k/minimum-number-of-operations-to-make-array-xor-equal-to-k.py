class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total = 0
        for x in nums:
            total^=x
        diff = total ^k
        return diff.bit_count()
        