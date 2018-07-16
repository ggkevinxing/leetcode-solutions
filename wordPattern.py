class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dict = {}
        patternList = list(pattern)
        print(patternList)
        words = str.split()
        if (len(patternList) != len(words)) or (len(set(patternList)) != len(set(words))):
            return False
        for i, word in enumerate(words):
            if dict.get(word) != None:
                if dict[word] != patternList[i]:
                    return False
            else:
                dict[word] = patternList[i]
        return True