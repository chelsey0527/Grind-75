# Merge Intervals

Problem can be found in [here](https://leetcode.com/problems/merge-intervals)!

### [solution](/Array/56-MergeIntervals/): Back Tracking

```python
class Solution(object):
    def merge(self, intervals):
        # Sort the intervals based on the start time
        intervals.sort(key=lambda x: x[0])
        
        # Initialize the result list with the first interval
        merged = [intervals[0]]
        
        # Iterate over the remaining intervals
        for interval in intervals[1:]:
            # If the current interval overlaps with the last merged interval, merge them
            if interval[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], interval[1])
            # If the current interval doesn't overlap, add it to the merged list
            else:
                merged.append(interval)
        
        return merged

```

Time Complexity: ![O(nlogn)](<https://latex.codecogs.com/svg.image?\inline&space;O(nlogn)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)


