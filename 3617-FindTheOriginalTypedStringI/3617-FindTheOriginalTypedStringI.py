# Last updated: 7/21/2026, 7:07:11 PM
class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        



        ans = 0
        for i in range(len(word)):
            if i == 0:
                ans += 1
            else:
                if word[i] != word[i-1]:
                    ans += 1
        return len(word) - ans +1