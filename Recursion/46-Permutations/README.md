# Permutations
Problem can be found in [here](https://leetcode.com/problems/permutations/)!

### [Solution](/Recursion/46-Permutations/solution.py)

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        if len(nums) == 1: return [nums[:]]

        for i in len(nums):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            
            res.extend(perms)
            nums.append(n)

        return res
```

Time Complexity: ![O(n^2)](<https://latex.codecogs.com/svg.image?\inline&space;O(n^2)>), Space Complexity: ![O(n^2)](<https://latex.codecogs.com/svg.image?\inline&space;O(n^2)>)


