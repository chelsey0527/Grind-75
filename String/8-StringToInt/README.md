# Contains Duplicate

Problem can be found in [here](https://leetcode.com/problems/string-to-integer-atoi/)!

### [solution](/String/8-StringToInt/README.md)

```python
class Solution(object):
    def myAtoi(self, s):
        ans = ''
        is_negative = False
        started = False

        for ss in s:
            if ss == ' ':
                if started:
                    break
                continue

            if ss.isdigit():
                ans += ss
                started = True
            elif ss == '-' and not started:
                is_negative = True
                started = True
            elif ss == '+' and not started:
                started = True
            else:
                break

        if ans == '':
            return 0

        result = int(ans)
        if is_negative:
            result = -result

        if result < -2 ** 31:
            return -2 ** 31
        elif result > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return result

```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

