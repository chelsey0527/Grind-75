class MinStack(object):
    def __init__(self):
        self.q = []
        self.min_stack = []  # Additional stack for minimum elements

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.q.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        if self.q:
            popped = self.q.pop()
            if popped == self.min_stack[-1]:
                self.min_stack.pop()
            return popped

    def top(self):
        """
        :rtype: int
        """
        if self.q:
            return self.q[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.min_stack:
            return self.min_stack[-1]
