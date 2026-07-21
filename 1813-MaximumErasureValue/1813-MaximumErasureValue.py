# Last updated: 7/21/2026, 7:08:44 PM
class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        cur_sum = 0
        start = 0
        seen = set()

        for end in range(len(nums)):
            while nums[end] in seen:
                seen.remove(nums[start])
                cur_sum -= nums[start]
                start += 1

            cur_sum += nums[end]
            seen.add(nums[end])

            res = max(res, cur_sum)

        return res