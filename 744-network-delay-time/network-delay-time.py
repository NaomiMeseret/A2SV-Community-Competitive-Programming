class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjacency = []
        for i in range(0, n + 1):
            adjacency.append([])
        for edge in times:
            u,v,w = edge[0], edge[1], edge[2]
            adjacency[u].append((v, w))
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        heap = []
        heapq.heappush(heap, (0, k))
        while len(heap) > 0:
            current = heapq.heappop(heap)
            d = current[0]
            node = current[1]
            if d > dist[node]:
                continue
            neighbors = adjacency[node]
            for item in neighbors:
                v,w = item[0],item[1]
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))
        ans = max(dist[1:])
        if ans == float('inf'):
            return -1
        else:
            return ans