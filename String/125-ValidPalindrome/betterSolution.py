import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        left = 0  # Pointer starting from the beginning of the string
        right = len(s) - 1  # Pointer starting from the end of the string

        while left < right:  # Continue until the pointers cross each other

            # Move the left pointer to the next alphanumeric character
            while left < right and not s[left].isalnum():
                left += 1

            # Move the right pointer to the next alphanumeric character
            while left < right and not s[right].isalnum():
                right -= 1

            if left < right and s[left].lower() != s[right].lower():
                # If the characters at the pointers don't match (case-insensitive),
                # return False since it's not a palindrome
                return False

            left += 1  # Move the left pointer forward
            right -= 1  # Move the right pointer backward

        return True  # If the loop completes without finding any mismatch, it's a palindrome
