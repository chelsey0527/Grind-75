# Ransom Note

Problem can be found in [here](https://leetcode.com/problems/ransom-note/)!

### [solution](/Hash%20Table/383-RansomNote/solution.py)

```python
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        st1, st2 = Counter(ransomNote), Counter(magazine)
        return st1 & st2 == st1
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>) for each