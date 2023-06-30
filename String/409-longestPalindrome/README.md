# Contains Duplicate

Problem can be found in [here](https://leetcode.com/problems/longest-palindrome/)!

### [solution](/String/409-longestPalindrome/): set

```python
class Solution(object):
    def longestPalindrome(self, s):

        ss = set()
        for letter in s:
            # All letter Must be a pair, otherwise will be record
            if letter not in ss:
                ss.add(letter)
            else:
                ss.remove(letter)
        if len(ss) != 0:
            # Calculate the rest which can be a pair and add the middle one(can be any).
            return len(s) - len(ss) + 1
        else:
            return len(s)  
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

