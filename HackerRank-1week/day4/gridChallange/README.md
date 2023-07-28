# Grid Challange

Problem can be found in [here](https://www.hackerrank.com/challenges/one-week-preparation-kit-grid-challenge/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D%5B%5D=one-week-day-four)!

### [solution](/HackerRank-1week/day4/gridChallange/solution.py)

```python
def gridChallenge(grid):
    # Sort items in each row
    for i in range(len(grid)):
        grid[i] = "".join(sorted(grid[i]))
        
    # Check if elements in each column are in ascending order
    for i in range(len(grid[0])):
        for j in range(len(grid) - 1):
            if grid[j][i] > grid[j + 1][i]:
                return "NO"
    
    return "YES"
```

Time Complexity: ![O(n^2)](<https://latex.codecogs.com/svg.image?\inline&space;O(n^2)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)