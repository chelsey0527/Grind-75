# Climbing Stairs
Problem can be found in [here](https://leetcode.com/problems/climbing-stairs/)!

### [Solution](/DynamicProgramming/70-ClimbingStairs/solution.pyy)

```python
class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 3:
            return n
        
        # In the left sub tree, we can get the base case: when 2 solution is 3, when 1 solution is 2
        # And all the rest subtree follow this pattern.
        n1, n2 = 2, 3

        for i in range (4, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp

        return n2

        # Bottom up dynamic programming
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)


