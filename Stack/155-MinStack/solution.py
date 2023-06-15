class MinStack(object):

    def __init__(self):
        self.q = deque()

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.q.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        #  for i in range(len(self.q)):

        return self.q.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.q[len(self.q) - 1]

    def getMin(self):
        """
        :rtype: int
        """
        min = self.q[0]

        for i in self.q:
            if i < min: min = i

        return min