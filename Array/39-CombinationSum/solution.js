/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function (candidates, target) {
    // Use an array to store all results
    const results = [];
    // Calling backtrack function to find suitable numbers
    backtrack(candidates, target, [], results);
    // Return answers
    return results;
}

var backtrack = function (candidates, target, current, results) {
    // If this is the last one, just push current and finish
    if (target === 0) {
        results.push([...current]);
        return;
    }

    // If sum < 0. terminate the current recursion branch
    if (target < 0) {
        return;
    }

    // Explore all candidates
    for (let i = 0; i < candidates.length; i++) {
        // Chose one candidate and add it into the current combination
        current.push(candidates[i]);
        // Recursive call: reduce the target by the chosen candidate and continue exploring
        // Pass a sliced version of candidates to avoid reusing the same candidate multiple times
        backtrack(candidates.slice(i), target - candidates[i], current, results);
        // Remove the last candidate from the current combination to backtrack and try other candidates
        current.pop();
    }
}

