class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum=0
        prefixSumCount={0:1}
        count=0
        for num in nums:
            prefixSum+=num
            if (prefixSum-k) in prefixSumCount:
                count+=prefixSumCount[prefixSum-k]
            prefixSumCount[prefixSum]=prefixSumCount.get(prefixSum,0)+1
        return count
        