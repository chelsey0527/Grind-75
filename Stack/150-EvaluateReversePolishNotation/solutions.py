class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

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