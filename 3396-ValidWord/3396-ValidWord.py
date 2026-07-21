# Last updated: 7/21/2026, 7:07:31 PM
class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) < 3:
            return False
        vowels = 0
        consonants = 0
        vowel_set = "aeiouAEIOU"
        for c in word:
            if c.isdigit():
                continue
            elif not c.isalpha():
                return False
            elif c in vowel_set:
                vowels += 1
            else:
                consonants += 1
        return vowels >= 1 and consonants >= 1
