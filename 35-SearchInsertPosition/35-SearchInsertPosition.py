# Last updated: 7/21/2026, 7:10:17 PM
def helper(nums,target):
    if len(nums)<1:
        return 0
    mid = len(nums)//2
    if target == nums[mid]:
        return mid
    elif target>nums[mid]:
        return mid+1+helper(nums[mid+1:],target)
    else:
        return helper(nums[:mid],target)


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        return helper(nums,target)

       