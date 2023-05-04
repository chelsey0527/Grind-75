# Contains Duplicate

Problem can be found in [here](https://leetcode.com/problems/contains-duplicate)!

### [solution 1](/Array/217-ContainsDuplicate/solutionMap.js): Map

```javascript
var containsDuplicate = function(nums) {
    const map = new Map();

    for( let i = 0; i < nums.length; i++){
        if (!map.has(nums[i])) {
            map.set(nums[i], i);
        } else {
            return true;
        }
    }

    return false;
    
};
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

### [solution 2 ](/Array/217-ContainsDuplicate/solutionSort.js): 

```javascript
var containsDuplicate = function(nums) {
    nums.sort((a, b) => a - b); // Sort before compare

    for (let i = 1; i < nums.length; i++) {
        if (nums[i] === nums[i - 1]) {
            return true;
        }
    }
    return false;
};

```

Time Complexity: ![O(nlogn)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)