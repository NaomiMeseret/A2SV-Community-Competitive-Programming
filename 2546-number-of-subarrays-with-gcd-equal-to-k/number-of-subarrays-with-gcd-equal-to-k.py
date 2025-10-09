class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            currGcd = 0
            for j in range(i,n):
                currGcd = gcd(currGcd , nums[j])
                if currGcd == k:
                    count +=1
                elif currGcd <k:
                    break
        return count

        