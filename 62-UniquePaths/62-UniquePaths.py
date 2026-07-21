# Last updated: 7/21/2026, 7:10:03 PM
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1)