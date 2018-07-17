class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x < 0:
            result = -(int(str(-x)[::-1]))
            if result < -2147483648:
                return 0
        else:
            result = int(str(x)[::-1])
            if result > 2147483647:
                return 0
        return result