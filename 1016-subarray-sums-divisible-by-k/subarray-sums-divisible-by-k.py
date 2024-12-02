class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixSum=0
        count=0
        countRem={0:1}
        for num in nums:
            prefixSum+=num
            rem=prefixSum%k
            if rem in countRem:
                count+=countRem[rem]
            countRem[rem]=countRem.get(rem,0)+1
        return count
        