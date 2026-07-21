# Last updated: 7/21/2026, 7:10:04 PM
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.rstrip()
        s=s.split()
        return(len(s[-1]))