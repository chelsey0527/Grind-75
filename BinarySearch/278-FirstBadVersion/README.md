# First Bad version

Problem can be found in [here](https://leetcode.com/problems/first-bad-version/)!

### [solution](/BinarySearch/278-FirstBadVersion/solution.py)

```python
class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        left, right = 0, n - 1
        while left <= right:
            mid = (left+right) //2

            if isBadVersion(mid) == False:
                left = mid + 1
            else:
                right = mid - 1

        return left
```

Time Complexity: ![O(logn)](<https://latex.codecogs.com/svg.image?\inline&space;O(logn)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>) for each