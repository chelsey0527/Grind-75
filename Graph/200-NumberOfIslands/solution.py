class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        island = 0

        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range(ROWS) and c in range(COLS) and grid[r][c] == '1' and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1' and (row, col) not in visited:
                    bfs(row, col)
                    island += 1

        return island