# Last updated: 7/21/2026, 7:08:09 PM
class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        k = n // 3

        left_mins = [0] * n
        right_maxs = [0] * n

        left_sum = 0
        max_heap = []
        for i in range(k):
            heapq.heappush(max_heap, -nums[i])
            left_sum += nums[i]
        left_mins[k - 1] = left_sum

        for i in range(k, n - k):
            if nums[i] < -max_heap[0]:
                left_sum += nums[i] + heapq.heappop(max_heap)
                heapq.heappush(max_heap, -nums[i])
            left_mins[i] = left_sum

        right_sum = 0
        min_heap = []
        for i in range(n - 1, n - k - 1, -1):
            heapq.heappush(min_heap, nums[i])
            right_sum += nums[i]
        right_maxs[n - k] = right_sum

        for i in range(n - k - 1, k - 2, -1):
            if nums[i] > min_heap[0]:
                right_sum += nums[i] - heapq.heappop(min_heap)
                heapq.heappush(min_heap, nums[i])
            right_maxs[i] = right_sum

        min_diff = float('inf')
        for i in range(k - 1, n - k):
            min_diff = min(min_diff, left_mins[i] - right_maxs[i + 1])

        return min_diff