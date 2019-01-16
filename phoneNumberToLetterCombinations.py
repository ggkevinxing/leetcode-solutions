class Solution(object):
    
    numDict = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    
    def letterCombinations_recurse(self, digits, currResults):
        if not digits:
            return currResults
        
        # take first digit, append all combinations to given results to make next results arr
        nextNum = digits[0]
        nextDigits = digits[1::]
        nextLetters = self.numDict[nextNum]
        nextResults = []
        
        for letterCombo in currResults:
            for letter in nextLetters:
                nextResults.append(letterCombo + letter)
        
        return self.letterCombinations_recurse(nextDigits, nextResults)
        
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        nextNum = digits[0]
        nextDigits = digits[1::]
        initResults = self.numDict[nextNum]
        
        return self.letterCombinations_recurse(nextDigits, initResults)
    