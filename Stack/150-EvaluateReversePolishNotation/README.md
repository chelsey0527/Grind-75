# Contains Duplicate

Problem can be found in [here](https://leetcode.com/problems/evaluate-reverse-polish-notation/)!

### [solution](/Stack/150-EvaluateReversePolishNotation/README.md)

```python
class Solution(object):
    def evalRPN(self, tokens):

        # Use stack to store calculation process
        stack = []

        for i in tokens :
            if i in ["+", "-", "*", "/"]:
                b = int(stack.pop())
                a = int(stack.pop())
                res = 0
                if (i == "+") : 
                    res = a + b
                elif (i=="-") : 
                    res = a - b
                elif (i=="*") : 
                    res = a * b
                elif (i == "/") :
                    res = int(float(a)/float(b))
                
                stack.append(res)
            else :
                stack.append(i)
        
        return int(stack.pop())
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>) for each