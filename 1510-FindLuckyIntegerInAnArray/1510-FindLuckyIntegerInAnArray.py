# Last updated: 7/21/2026, 7:08:50 PM
from collections import Counter

class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        counts = Counter(arr)
        lucky = -1
        for num, count in counts.items():
            if num == count:
                lucky = max(lucky, num)
        return lucky