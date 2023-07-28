# Recursive Digit Sum

Problem can be found in [here](https://www.hackerrank.com/challenges/one-week-preparation-kit-recursive-digit-sum/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D%5B%5D=one-week-day-four)!

### [solution](/HackerRank-1week/day4/RecursiveDigitSum/solution.py)

```python
def superDigit(n, k):
        
    # check single digits
    if k == len(n) == 1:
        return int(n)

    res = 0
    for num in n:
        res += int(num)
    
    return superDigit(str(res*k),1)
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)