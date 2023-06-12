class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
 
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