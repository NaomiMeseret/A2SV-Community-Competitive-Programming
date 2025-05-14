class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        totalSubsets = 1<<n
        res = []
        for mask in range(totalSubsets):
            subset = []
            for i in range(n):
                if mask & (1<<i) !=0:
                    subset.append(nums[i])
            res.append(subset)
        return res

        