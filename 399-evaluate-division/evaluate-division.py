class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (a,b) , val in zip(equations , values):
            graph[a][b] = val
            graph[b][a] = 1.0/val
        def dfs(start , end):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            visted = set()
            stack = [(start , 1.0)]
            while stack :
                node , prod = stack.pop()
                if node == end:
                    return prod
                visted.add(node)
                for nei , w in graph[node].items():
                    if nei in visted:
                        continue
                    stack . append((nei , prod*w))
            return -1.0
        return [dfs(c,d) for c , d in queries]

        