# Insert Interval

Problem can be found in [here](https://leetcode.com/problems/insert-interval/)!

### [solution 1](/Array/57-InsertInterval/solution.py): Linear Scanning & DP

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # End value of the interval is smaller than the start value
            if newInterval[1] < intervals[i][0]:
                print(newInterval[1], '< ', intervals[i][0])
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                print(newInterval[0], '> ', intervals[i][1])
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
                print('new interval', newInterval)
            print(res)  
            print('---')

        res.append(newInterval)
            
        return res
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)