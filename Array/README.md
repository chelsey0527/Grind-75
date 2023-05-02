# Two Sum

Problem can be found in [here](https://leetcode.com/problems/two-sum/)!

### [Solution](/Array/1-TwoSum/solution.js): Brute Force

```javascript
var twoSum = function(nums, target) {
  let a = [];  // Use an array to store result

  for (let i = 0; i < nums.length; i++){
      for (let j = nums.length-1; j > i; j--){
          if (nums[i] + nums[j] === target){
              a.push(i);
              a.push(j);
          }
      }
  }
  return a;
};
```

Time Complexity: ![O(n^2)](<https://latex.codecogs.com/svg.image?\inline&space;O(n^2)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

Explanation: Simply iterate the array and find the target value among the array in each iteration.

<!-- ### [Improved Solution](/Array/1-TwoSum/improvedSolution.py): Hash Table

```python
memo = {}
for i, j in enumerate(nums):
    number_to_find = target - j
    try:
        return [memo[j], i] # Find indices of the two numbers!
    except KeyError:
        memo[number_to_find] = i
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

Explanation: Instead of searching the whole array blindlessly in each iteration, using a hash table can determine whether this element is the target value in ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>) time. -->