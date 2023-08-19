# Contains Duplicate

Problem can be found in [here](https://leetcode.com/problems/contains-duplicate)!


### [solution](/Array/217-ContainsDuplicate/solution.py): Sort

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]: return True

        return False
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)