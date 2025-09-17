class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        stack = []
        for i in range(m):
            if board[i][0] == 'O':
                stack.append((i, 0)); board[i][0] = '#'
            if board[i][n-1] == 'O':
                stack.append((i, n-1)); board[i][n-1] = '#'
        for j in range(n):
            if board[0][j] == 'O':
                stack.append((0, j)); board[0][j] = '#'
            if board[m-1][j] == 'O':
                stack.append((m-1, j)); board[m-1][j] = '#'
        while stack:
            r, c = stack.pop()
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'O':
                    stack.append((nr, nc))
                    board[nr][nc] = '#'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'