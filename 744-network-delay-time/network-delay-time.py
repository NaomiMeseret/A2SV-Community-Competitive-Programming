class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((w, v))
        heap = [(0, k)]
        visited = set()
        time = 0
        while heap:
            t, u = heapq.heappop(heap)
            if u in visited:
                continue
            visited.add(u)
            time = t
            for w, v in graph[u]:
                if v not in visited:
                    heapq.heappush(heap, (t + w, v))
        if len(visited) == n:
            return time 
        else:
            return -1