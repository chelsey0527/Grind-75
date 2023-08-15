# Min stack

Problem can be found in [here](https://leetcode.com/problems/min-stack/)!

### [solution](/Stack/155-MinStack/solution.py)

```python
class MinStack(object):

    def __init__(self):
        self.q = deque()

    def push(self, val):
        self.q.append(val)
        
    def pop(self):
        return self.q.pop()
        
    def top(self):
        return self.q[len(self.q) - 1]

    def getMin(self):
        min = self.q[0]

        for i in self.q:
            if i < min: min = i

        return min
    
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>) for each


## [better solution](/Stack/155-MinStack/betterSolution.py)

```python
class MinStack(object):
    def __init__(self):
        self.q = []
        self.min_stack = []  # Additional stack for minimum elements

    def push(self, val):
        self.q.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.q:
            popped = self.q.pop()
            if popped == self.min_stack[-1]:
                self.min_stack.pop()
            return popped

    def top(self):
        if self.q:
            return self.q[-1]

    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]
```


Time Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>) for each

In this updated implementation, the min_stack is used to store the minimum elements. Whenever a new element is pushed onto the stack, it is compared with the top element of the min_stack. If it is smaller or equal, it is also pushed onto the min_stack. This way, the min_stack always keeps track of the minimum element at the top.
