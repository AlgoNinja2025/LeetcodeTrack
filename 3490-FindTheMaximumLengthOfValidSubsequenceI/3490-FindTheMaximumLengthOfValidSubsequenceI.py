# Last updated: 7/21/2026, 7:07:27 PM
class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        if not nums:
            return 0
        
        c = nums[0] % 2
        odd = even = both = 0
        for num in nums:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1
            if num % 2 == c:
                both += 1
                c = 1 - c
        return max(both, even, odd)
