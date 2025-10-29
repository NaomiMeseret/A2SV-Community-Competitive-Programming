class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        if start_node == end_node:
            return 1.0
        g = [[] for _ in range(n)]
        for i in range(len(edges)):
            u,v = edges[i]
            p = succProb[i]
            g[u].append((v,p))
            g[v].append((u,p))
        res = [0.0]*n
        res[start_node] = 1.0
        heap = [(-1.0, start_node)]
        while heap:
            prob , u = heapq.heappop(heap)
            prob = -prob
            if prob <res[u]:
                continue
            if u== end_node:
                return prob
            for v,p in g[u]:
                np  = prob *p
                if np >res[v]:
                    res[v] = np
                    heapq.heappush(heap,(-np ,v))
        return 0.0
        