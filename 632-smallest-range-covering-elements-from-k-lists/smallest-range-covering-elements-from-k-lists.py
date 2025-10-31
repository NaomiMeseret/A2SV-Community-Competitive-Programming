class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        k = len(nums)
        merged = []
        for i in range(k):
            for v in nums[i]:
                merged.append((v, i))
        merged.sort()
        n = len(merged)
        count = [0] * k
        have = 0
        left = 0
        best_len = float("inf")
        best_l = 0
        best_r = float("inf")

        for right in range(n):
            val, idx = merged[right]
            if count[idx] == 0:
                have += 1
            count[idx] += 1

            while have == k:
                lval, lidx = merged[left]
                cur_len = val - lval
                if cur_len < best_len or (cur_len == best_len and lval < best_l):
                    best_len = cur_len
                    best_l = lval
                    best_r = val
                count[lidx] -= 1
                if count[lidx] == 0:
                    have -= 1
                left += 1

        return [best_l, best_r]

        