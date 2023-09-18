# Subsets
Problem can be found in [here](https://leetcode.com/problems/subsets/)!

### [Solution](/Recursion/78-Subsets/solution.py)

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # decision to include the node
            subset.append(nums[i])
            dfs(i + 1)

            # decision not to include the node
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res
```

Time Complexity: ![O(2^n)](<https://latex.codecogs.com/svg.image?\inline&space;O(2^n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)


