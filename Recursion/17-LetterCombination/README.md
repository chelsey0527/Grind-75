# Letter Combinations of a Phone Number
Problem can be found in [here](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)!

### [Solution](/Recursion/17-LetterCombination/)

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

Time Complexity: ![O(4^n)](<https://latex.codecogs.com/svg.image?\inline&space;O(4^n)>), Space Complexity: ![O(4^n)](<https://latex.codecogs.com/svg.image?\inline&space;O(4^n)>)


