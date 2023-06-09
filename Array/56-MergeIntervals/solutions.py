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
