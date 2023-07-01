# Contains Duplicate

Problem can be found in [here](https://leetcode.com/problems/longest-substring-without-repeating-characters/)!

### [solution](/String/3-LongestSubstringWithoutRepeatingChars/solution.py): sliding window

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {}
        l = 0
        output = 0

        for r in range(len(s)):
            if s[r] not in seen:
                output = max(output,r-l+1)
            else:
                if seen[s[r]] < l:
                    output = max(output,r-l+1)
                else:
                    l = seen[s[r]] + 1
            seen[s[r]] = r
            
        return output 
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

