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


// This output will be helpful for understanding
/**
push:  2
current:  [ 2 ]  rm-cand:  5  i:  0
push:  2
current:  [ 2, 2 ]  rm-cand:  3  i:  0
push:  2
current:  [ 2, 2, 2 ]  rm-cand:  1  i:  0
push:  2
current:  [ 2, 2, 2, 2 ]  rm-cand:  -1  i:  0
rm < 0
pop:  [ 2, 2, 2, 2 ]

push:  3
current:  [ 2, 2, 2, 3 ]  rm-cand:  -2  i:  1
rm < 0
pop:  [ 2, 2, 2, 3 ]

push:  6
current:  [ 2, 2, 2, 6 ]  rm-cand:  -5  i:  2
rm < 0
pop:  [ 2, 2, 2, 6 ]

push:  7
current:  [ 2, 2, 2, 7 ]  rm-cand:  -6  i:  3
rm < 0
pop:  [ 2, 2, 2, 7 ]

pop:  [ 2, 2, 2 ]

push:  3
current:  [ 2, 2, 3 ]  rm-cand:  0  i:  1
rm == 0
push into result;
pop:  [ 2, 2, 3 ]

push:  6
current:  [ 2, 2, 6 ]  rm-cand:  -3  i:  2
rm < 0
pop:  [ 2, 2, 6 ]

push:  7
current:  [ 2, 2, 7 ]  rm-cand:  -4  i:  3
rm < 0
pop:  [ 2, 2, 7 ]

pop:  [ 2, 2 ]

push:  3
current:  [ 2, 3 ]  rm-cand:  2  i:  1
push:  3
current:  [ 2, 3, 3 ]  rm-cand:  -1  i:  1
rm < 0
pop:  [ 2, 3, 3 ]

push:  6
current:  [ 2, 3, 6 ]  rm-cand:  -4  i:  2
rm < 0
pop:  [ 2, 3, 6 ]

push:  7
current:  [ 2, 3, 7 ]  rm-cand:  -5  i:  3
rm < 0
pop:  [ 2, 3, 7 ]

pop:  [ 2, 3 ]

push:  6
current:  [ 2, 6 ]  rm-cand:  -1  i:  2
rm < 0
pop:  [ 2, 6 ]

push:  7
current:  [ 2, 7 ]  rm-cand:  -2  i:  3
rm < 0
pop:  [ 2, 7 ]

pop:  [ 2 ]

push:  3
current:  [ 3 ]  rm-cand:  4  i:  1
push:  3
current:  [ 3, 3 ]  rm-cand:  1  i:  1
push:  3
current:  [ 3, 3, 3 ]  rm-cand:  -2  i:  1
rm < 0
pop:  [ 3, 3, 3 ]

push:  6
current:  [ 3, 3, 6 ]  rm-cand:  -5  i:  2
rm < 0
pop:  [ 3, 3, 6 ]

push:  7
current:  [ 3, 3, 7 ]  rm-cand:  -6  i:  3
rm < 0
pop:  [ 3, 3, 7 ]

pop:  [ 3, 3 ]

push:  6
current:  [ 3, 6 ]  rm-cand:  -2  i:  2
rm < 0
pop:  [ 3, 6 ]

push:  7
current:  [ 3, 7 ]  rm-cand:  -3  i:  3
rm < 0
pop:  [ 3, 7 ]

pop:  [ 3 ]

push:  6
current:  [ 6 ]  rm-cand:  1  i:  2
push:  6
current:  [ 6, 6 ]  rm-cand:  -5  i:  2
rm < 0
pop:  [ 6, 6 ]

push:  7
current:  [ 6, 7 ]  rm-cand:  -6  i:  3
rm < 0
pop:  [ 6, 7 ]

pop:  [ 6 ]

push:  7
current:  [ 7 ]  rm-cand:  0  i:  3
rm == 0
push into result;
pop:  [ 7 ]

 */
