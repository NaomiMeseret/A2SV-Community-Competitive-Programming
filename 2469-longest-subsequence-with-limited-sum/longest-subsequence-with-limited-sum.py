class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans = []
        for q in queries:
            prefixSum = 0
            count = 0
            for num in nums:
                if prefixSum + num <= q:
                    prefixSum += num
                    count += 1
                else:
                    break
            ans.append(count)
        return ans