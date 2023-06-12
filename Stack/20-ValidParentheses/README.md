# Contains Duplicate

Problem can be found in [here](https://leetcode.com/problems/valid-parentheses/)!

### [solution 1](/Stack/20-ValidParentheses/solution.py): Stack and Hashmap

```python
class Solution(object):
    def isValid(self, s):"
 
        stack = []
        # Using Hashmap to match all open to correspond close
        closeToOpen = {')': '(', '}': '{', ']': '['}

        # Check if the string is odd, if so, return False directly
        if len(s) % 2 != 0: 
            return False

        for char in s:
            # If char is an closing parentheses
            if char in closeToOpen:
                # Make sure stack is not empty and value on the top of stack is the matching value
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)