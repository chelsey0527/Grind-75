# Majority Element

Problem can be found in [here](https://leetcode.com/problems/majority-element/)!

### [solution](/Array/169-MajorityElement//solutionSort.js): Sort

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        nums = sorted(nums)
        return nums[len(nums)//2]
```

Time Complexity: ![O(nlogn)](<https://latex.codecogs.com/svg.image?\inline&space;O(nlogn)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)
