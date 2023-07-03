class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
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
