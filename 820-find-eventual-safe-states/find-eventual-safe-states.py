class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        order = []
        colors = [0 for _ in range(len(graph))]
        def dfs(node):
            if colors[node] == 1:
                return False
            if colors[node] == 2:
                return True
            colors[node] = 1
            for neigh in graph[node]:
                if not dfs(neigh):
                    return False
            colors[node] = 2
            order.append(node)
            return True
        for node in range(len(graph)):
            if colors[node] == 0:
                dfs(node)
        order.sort()
        return order
