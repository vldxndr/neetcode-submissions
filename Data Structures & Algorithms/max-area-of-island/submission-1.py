class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        res = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxIsland = 1
                    stack = [(r, c)]
                    visited.add((r, c))

                    while stack:
                        curr_r, curr_c = stack.pop()

                        for dr, dc in dirs:
                            nr = dr + curr_r
                            nc = dc + curr_c

                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr, nc) not in visited:
                                stack.append((nr, nc))
                                visited.add((nr, nc))
                                maxIsland += 1

                    res = max(res, maxIsland)
        return res
