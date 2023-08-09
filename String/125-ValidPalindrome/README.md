# Valid Palindrome

Problem can be found in [here](https://leetcode.com/problems/valid-palindrome/)!

### [solution](/String/125-ValidPalindrome/solution.py)

```python
class Solution(object):
    def isPalindrome(self, s):

        # Change the string into desired format
        cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        # Return true while there is only one or none character
        if len(cleaned_string) <= 1:
            return True

        # Use left and right pointers
        left = 0
        right = len(cleaned_string)-1

        while left < :
            if cleaned_string[left] != cleaned_string[right]:
                return False
            left += 1
            right -= 1

        return True
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

### [better space complexity solution](/String/125-ValidPalindrome/betterSolution.py)

```python
import re

class Solution(object):
    def isPalindrome(self, s):

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

```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)
