# Last updated: 7/21/2026, 7:08:21 PM
class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        return sum(1 if op[1]=='+' else -1 for op in operations)