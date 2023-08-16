# Binary Search

Problem can be found in [here](https://leetcode.com/problems/binary-search/)!

### [solution](/BinarySearch/704-BinarySearch/solution.py)

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        for i in range(len(nums)//2+1):
            if nums[i] == target: return i
            if nums[len(nums) - 1 - i] == target: return len(nums) - 1 - i

        return -1
```

### Better solution: Update the right or left side with mid.
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(l, r):
            while l <= r:
                mid = (l + r) >> 1
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
            return - 1

        return binary_search(0, len(nums) - 1)
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>) for each