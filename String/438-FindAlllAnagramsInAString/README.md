# Find Alll Anagrams In A String


Problem can be found in [here](https://leetcode.com/problems/find-all-anagrams-in-a-string/)!

### [solution](/String/438-FindAlllAnagramsInAString/solution.py): Sliding window

```python
class Solution(object):
    def findAnagrams(self, s, p):

        # return empty list when p is larger than s
        if len(p) > len(s):
            return []
        
        # initialize our hashmap
        pCount, sCount = {}, {}
        
        # Check the first len(p) element
        for i in range(len(p)):
            pCount[p[i]] = pCount.get(p[i], 0) + 1
            sCount[s[i]] = sCount.get(s[i], 0) + 1
        
        # we may add first position while the loop up found the count is same
        res = [0] if sCount == pCount else []
        l = 0

        # Sliding window
        for r in range(len(p), len(s)):
            # use get to initialize value to prevent type error
            sCount[s[r]] = sCount.get(s[r], 0) + 1
            sCount[s[l]] -= 1
            
            # pop out the first element
            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            
            # move to next element
            l += 1

            # append into res when count are equal
            if sCount == pCount:
                res.append(l)
        
        return res
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

