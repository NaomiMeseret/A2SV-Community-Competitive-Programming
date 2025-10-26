class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph)-1
        q = deque([[0]])
        res = []
        while q:
            path = q.popleft()
            node = path[-1]
            if node == target:
                res.append(path)
            else:
                for nei in graph[node]:
                    q.append(path+[nei])
        return res

        