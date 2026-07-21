# Last updated: 7/21/2026, 7:09:18 PM
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        count = collections.Counter(nums)

        for num, freq in count.items():
            if num + 1 in count:
                ans = max(ans, freq + count[num + 1])

        return ans