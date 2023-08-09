# Valid Anagram

Problem can be found in [here](https://leetcode.com/problems/valid-anagram/)!

### [solution](/String/242_ValidAnagram/solution.py)

```python
class Solution(object):
    def isAnagram(self, s, t):

        if sorted(s) == sorted(t):
            return True
        
        return False
        
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(nlogn)](<https://latex.codecogs.com/svg.image?\inline&space;O(nlogn)>)

### [better space complexity solution](/String/242_ValidAnagram/betterSolution.py) Flag

```python
class Solution(object):
    def isAnagram(self, s, t):

        flag = True

        if len(s) != len(t): 
            flag = False
        else:
            letters = "abcdefghijklmnopqrstuvwxyz"
            for letter in letters:
                if s.count(letter) != t.count(letter):
                    flag = False
                    break

        return flag

```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)
