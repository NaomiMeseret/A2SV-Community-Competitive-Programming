class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xor_totals = [0]
        for num in nums:
            xor_totals +=[x^num for x in xor_totals]
        return sum(xor_totals)