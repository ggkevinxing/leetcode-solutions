class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # make sure they're in order first
        g.sort()
        s.sort()
        
        gInd = 0
        sInd = 0
        
        # greedy approach
        while gInd < len(g) and sInd < len(s):
            if g[gInd] <= s[sInd]:
                gInd += 1
            sInd += 1
            
        return gInd
