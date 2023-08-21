# Combination Sum

Problem can be found in [here](https://leetcode.com/problems/combination-sum)!

### [solution](/Array/39-CombinationSum/README.md): Back Tracking

```javascript
var combinationSum = function(candidates, target) {
    const results = [];
    
    const backtrack = function(current, remaining, start) {
        if (remaining < 0) {
            return;
        }
        
        if (remaining === 0) {
            results.push([...current]);
            return;
        }
        
        for (let i = start; i < candidates.length; i++) {
            current.push(candidates[i]);
            backtrack(current, remaining - candidates[i], i);
            current.pop();
        }
    };
    
    backtrack([], target, 0);
    
    return results;
};
```

Time Complexity: ![O(n^n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n^n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)


