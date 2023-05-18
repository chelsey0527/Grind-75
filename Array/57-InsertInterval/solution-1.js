/**
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]}
 */
var insert = function(intervals, newInterval) {
  let [start, end] = newInterval;
  let result = [];

  let i = 0;

  // Add intervals that come before the newInterval
  while (i < intervals.length && intervals[i][1] < start) {
    result.push(intervals[i]);
    i++;
  }

  // Merge overlapping intervals (we only need the last one)
  while (i < intervals.length && intervals[i][0] <= end) {
    // In each round, we only want the min of the start and max of the end
    start = Math.min(start, intervals[i][0]);
    end = Math.max(end, intervals[i][1]);
    i++;
  }
  result.push([start, end]);

  // Add remaining intervals
  while (i < intervals.length) {
    result.push(intervals[i]);
    i++;
  }

  return result;
};
