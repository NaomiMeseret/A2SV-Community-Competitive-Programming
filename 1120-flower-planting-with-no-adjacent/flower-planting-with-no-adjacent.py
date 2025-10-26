class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in paths:
            graph[u].append(v)
            graph[v].append(u)

        result = [0] * n

        for i in range(1, n + 1):
            if result[i - 1] != 0:
                continue

            q = deque([i])
            while q:
                node = q.popleft()
                if result[node - 1] != 0:
                    continue

                flowers = {1, 2, 3, 4}
                for nei in graph[node]:
                    if result[nei - 1] in flowers:
                        flowers.remove(result[nei - 1])

                result[node - 1] = flowers.pop()

                for nei in graph[node]:
                    if result[nei - 1] == 0:
                        q.append(nei)

        return result