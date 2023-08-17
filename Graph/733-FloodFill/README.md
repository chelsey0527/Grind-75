# Flood Fill

Problem can be found in [here](https://leetcode.com/problems/flood-fill/description/)!

### [solution](/Graph/733-FloodFill/solution.py)

```python
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        # The point that starts to flood
        startColor = image[sr][sc]

        # Total rows and cols of the matrix
        rows, cols = len(image), len(image[0])

        def backtrack(i, j, grid):
            # Reject for invalid coordination
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return
            # Repeated traversal, or different color
            if grid[i][j] == color or startColor != grid[i][j]:
                return

            # Update color   
            grid[i][j] = color

            # DFS to connected neighbors 
            backtrack(i-1, j, grid)
            backtrack(i, j-1, grid)
            backtrack(i+1, j, grid)
            backtrack(i, j+1, grid)

        backtrack(sr,sc,image)
        return image
```

Time Complexity: ![O(m*n)](<https://latex.codecogs.com/svg.image?\inline&space;O(m*n)>), Space Complexity: ![O(m*n)](<https://latex.codecogs.com/svg.image?\inline&space;O(m*n)>) for each