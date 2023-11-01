# Rotting Oranges
Problem can be found in [here](https://leetcode.com/problems/rotting-oranges/)!

### [solution](/Graph/994-RottingOranges/)

```python
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if rows == 0: return -1

        rotten = deque()
        fresh_count = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    rotten.append((row, col))
                elif grid[row][col] == 1:
                    fresh_count += 1

        min_time = 0

        while rotten and fresh_count > 0:
            min_time += 1
            for _ in range(len(rotten)):
                row, col = rotten.popleft()
                for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    newRow, newCol = row + dx, col + dy
                    if newRow < 0 or newRow == rows or newCol < 0 or newCol == cols:
                        continue
                    if grid[newRow][newCol] == 2 or grid[newRow][newCol] == 0:
                        continue
                    fresh_count -= 1
                    grid[newRow][newCol] = 2
                    rotten.append((newRow, newCol))

        return min_time if fresh_count == 0 else -1

```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>) , Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

