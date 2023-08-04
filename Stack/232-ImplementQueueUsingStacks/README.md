# Implement Queue Using Stacks

Problem can be found in [here](https://leetcode.com/problems/implement-queue-using-stacks/)!

### [solution 1](/Stack/232-ImplementQueueUsingStacks/)

```python
class MyQueue(object):

    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        
    def pop(self):
        for i in range(len(self.q)):
            return self.q.popleft()

    def peek(self):
        return self.q[0]
        

    def empty(self):
        return len(self.q) == 0
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>) for each
