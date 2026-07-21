# Last updated: 7/21/2026, 7:09:10 PM
class Solution(object):
    def subarrayBitwiseORs(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        result = set()
        current = set()
        for num in arr:
            current = {num | prev for prev in current} | {num}
            result.update(current)
        return len(result)