class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        ss = set()
        for letter in s:
            # All letter Must be a pair, otherwise will be record
            if letter not in ss:
                ss.add(letter)
            else:
                ss.remove(letter)
        if len(ss) != 0:
            # Calculate the rest which can be a pair and add the middle one(can be any).
            return len(s) - len(ss) + 1
        else:
            return len(s)