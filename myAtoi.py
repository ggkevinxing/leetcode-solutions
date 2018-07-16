class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        res = 0
        mult = 1
        s = str.strip()
        print(s)
        ind = 0
        for i in range(ind, len(s)):
            if s[i] == '-':
                mult = -1
                ind = i+1
                break
            elif s[i] == '+':
                ind = i+1
                break
            elif s[i].isnumeric() == True:
                ind = i
                break
            else:
                return res
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        for i in range(ind, len(s)):
            if s[i].isnumeric() == False:
                return res*mult
            else:
                res = res*10 + int(s[i])
                if res*mult > INT_MAX:
                    return INT_MAX
                elif res*mult < INT_MIN:
                    return INT_MIN
        return res*mult
            
            
        