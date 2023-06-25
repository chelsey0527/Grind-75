class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        # Return true while there is only one or none character
        if len(cleaned_string) <= 1:
            return True

        left = 0
        right = len(cleaned_string)-1

        while left != (len(cleaned_string)/2):
            if cleaned_string[left] != cleaned_string[right]:
                return False
            left += 1
            right -= 1

        return True