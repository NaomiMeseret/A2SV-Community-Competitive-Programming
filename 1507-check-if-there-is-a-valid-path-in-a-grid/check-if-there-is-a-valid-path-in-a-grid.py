class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return True
        conn = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)],
        }
        visited = [[False] * n for _ in range(m)]
        stack = [(0, 0)]
        visited[0][0] = True
        while stack:
            r, c = stack.pop()
            if r == m - 1 and c == n - 1:
                return True
            for dr, dc in conn[grid[r][c]]:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                if visited[nr][nc]:
                    continue
                if (-dr, -dc) not in conn[grid[nr][nc]]:
                    continue
                visited[nr][nc] = True
                stack.append((nr, nc))

        return False