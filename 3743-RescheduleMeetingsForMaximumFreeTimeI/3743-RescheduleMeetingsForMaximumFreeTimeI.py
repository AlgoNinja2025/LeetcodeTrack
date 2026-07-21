# Last updated: 7/21/2026, 7:07:02 PM
class Solution(object):
    def maxFreeTime(self, eventTime, k, startTime, endTime):
        """
        :type eventTime: int
        :type k: int
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        """
        def window(nums, k):
            sum_val = sum(nums[:k])
            max_sum = sum_val
            for i in range(k, len(nums)):
                sum_val = sum_val + nums[i] - nums[i - k]
                max_sum = max(max_sum, sum_val)
            return max_sum

        space = [0] * (len(startTime) + 1)
        n = len(startTime)
        prev = 0

        for i in range(n):
            space[i] = startTime[i] - prev
            prev = endTime[i]
        space[n] = eventTime - prev

        if k + 1 > len(space):
            return -1  

        result = window(space, k + 1)
        return result
