class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        charToDigit = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def backtrack(i, charStr):
            if len(charStr) == len(digits):
                res.append(charStr)
                return
            for c in charToDigit[digits[i]]:
                print(c)
                backtrack(i + 1, charStr + c)
            
        if digits:
            backtrack(0, "")
        return res