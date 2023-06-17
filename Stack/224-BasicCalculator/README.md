# Contains Duplicate

Problem can be found in [here](https://leetcode.com/problems/basic-calculator/)!

### [solution](/Stack/224-BasicCalculator/README.md)

```python
class Solution(object):
    def calculate(self, s):
       
      ans = 0
      num = 0
      sign = 1
      stack = [sign]  # stack[-1]: current env's sign

      for c in s:
        # If the character c is a digit, it enters this block. It converts the character to an integer using ord(c) - ord('0') and adds it to the num variable. This allows the code to handle numbers with multiple digits. The digits are extracted and accumulated in num by multiplying the existing value by 10 and adding the new digit.
        if c.isdigit():
          num = num * 10 + (ord(c) - ord('0'))
        # If the character c is an opening parenthesis '(', it means a new subexpression is starting. The current sign is pushed onto the stack to preserve it for the inner level of parentheses.
        elif c == '(':
          stack.append(sign)
        # If the character c is a closing parenthesis ')', it means the current subexpression is ending. The topmost element is popped from the stack as it represents the sign of the completed subexpression.
        elif c == ')':
          stack.pop()
        #   If the character c is either a plus '+' or minus '-' sign, it means a new operator is encountered. The current num is added to the running sum ans, taking into account the current sign sign. Then, the sign variable is updated based on the encountered operator (1 for '+', -1 for '-') and the topmost element of the stack. This ensures that the correct sign is applied based on the level of nested parentheses. Finally, num is reset to 0 to start accumulating the next number.
        elif c == '+' or c == '-':
          ans += sign * num
          sign = (1 if c == '+' else -1) * stack[-1]
          num = 0
    # After iterating through all the characters in the input string, the code adds the last num to the final sum ans, considering the last encountered sign sign. The calculated result ans is returned as the output of the calculate method.
    return ans + sign * num
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>) for each