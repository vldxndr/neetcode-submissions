class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        visited = set()
        nr_islands = 0
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == "1":
                    nr_islands += 1
                    stack = [(r, c)]
                    visited.add((r, c))

                    while stack:
                        curr_r, curr_c = stack.pop()

                        for dr, dc in dirs:
                            nr, nc = dr + curr_r, dc + curr_c

                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and (nr, nc) not in visited:
                                visited.add((nr, nc))

                                stack.append((nr, nc))
        return nr_islands