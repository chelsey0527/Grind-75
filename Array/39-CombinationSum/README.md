# Combination Sum

Problem can be found in [here](https://leetcode.com/problems/combination-sum)!

### [solution](/Array/39-CombinationSum/solution.py)

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
```

Time Complexity: ![O(n^n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n^n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)


