class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        sm = 0   
        queue = deque()
        res = inf
       
        for r in range(len(nums)):

            sm += nums[r]

            if sm >= k:
                res = min(res, r + 1)

            curr = None
            while queue and sm - queue[0][1] >= k:
                curr = queue.popleft()

            if curr:
                res = min(res, r - curr[0])

            while queue and queue[-1][1] >= sm:
                queue.pop()
            
            queue.append((r, sm))
    
        return res if res != inf else -1

        