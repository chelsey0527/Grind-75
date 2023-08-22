# Unique Paths

Problem can be found in [here](https://leetcode.com/problems/unique-paths/)!

### [solution](/DynamicProgramming/62-UniquePaths/solution.py)

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow

        return row[0]         
```

Time Complexity: ![O(m^n)](<https://latex.codecogs.com/svg.image?\inline&space;O(m^n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)
