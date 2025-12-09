class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        right = Counter(nums)
        left = Counter()
        ans = 0
        for j in range(len(nums)):
            x = nums[j]
            right[x] -= 1
            if right[x] == 0:
                del right[x]
            need = x * 2
            ans = (ans + left.get(need, 0) * right.get(need, 0)) % MOD
            left[x] += 1
        return ans
        