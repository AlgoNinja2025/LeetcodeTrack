# Last updated: 7/21/2026, 7:09:44 PM
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal = []                     # Initialize Pascal's Triangle list
        for i in range(numRows):
            row = [1] * (i + 1)         # First and last elements are always 1
            for j in range(1, i):       # Calculate inner elements
                row[j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
            pascal.append(row)          # Add the row to Pascal's Triangle
        return pascal