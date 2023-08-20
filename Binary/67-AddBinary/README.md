# Add Binary

Problem can be found in [here](https://leetcode.com/problems/add-binary/)!

### [Solution](/Binary/67-AddBinary/solution.py)

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        s = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        while i>=0 or j>=0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            s.append(str(carry%2))
            carry //= 2

        return ''.join(reversed(s))
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)


