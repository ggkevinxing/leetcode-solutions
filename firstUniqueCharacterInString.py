class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # build sets for all chars in s and
        # all repeated chars in s
        charsIn = set()
        charsRepeated = set()
        for c in s:
            if c in charsIn:
                charsRepeated.add(c)
            if c not in charsIn:
                charsIn.add(c)
        
        # take set difference between all chars in s and
        # repeated chars in s to get unique chars in s
        uniques = charsIn.difference(charsRepeated)
        if not uniques:
            return -1
        
        # find lowest index for every char in uniques
        # pick lowest index of them to get result
        minIndex = float('inf')
        for c in uniques:
            ind = s.index(c)
            if ind < minIndex:
                minIndex = ind
                
        return minIndex
