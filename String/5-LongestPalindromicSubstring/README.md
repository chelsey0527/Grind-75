# Contains Duplicate

Problem can be found in [here](https://leetcode.com/problems/longest-palindromic-substring/)!

### [solution](/String/5-LongestPalindromicSubstring/README.md): 

```python
class Solution(object):
    def longestPalindrome(self, s):

        n = len(s)
        
        def getLen(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1

        start = 0
        length = 0

        for i in range(n):
            cur = max(getLen(i, i), getLen(i, i + 1))
            
            if cur <= length: continue
            length = cur
            start = i - (cur - 1) // 2

        return s[start :  start + length]
        
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

