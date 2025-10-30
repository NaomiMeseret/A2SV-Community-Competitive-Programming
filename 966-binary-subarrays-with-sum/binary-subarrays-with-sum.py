class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixSum = 0
        prefixSumCount = {0:1}
        count = 0
        for num in nums:
            prefixSum +=num
            if (prefixSum-goal) in prefixSumCount:
                count +=prefixSumCount[prefixSum-goal]
            prefixSumCount[prefixSum] = prefixSumCount.get(prefixSum , 0)+1
        return count
        