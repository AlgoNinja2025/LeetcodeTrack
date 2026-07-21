# Last updated: 7/21/2026, 7:09:23 PM
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[-(k % len(nums)):] + nums[:-(k % len(nums))]