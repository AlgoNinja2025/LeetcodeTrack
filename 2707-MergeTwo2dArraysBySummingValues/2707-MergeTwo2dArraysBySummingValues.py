# Last updated: 7/21/2026, 7:07:50 PM
class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        merged = defaultdict(int)
        for k , v in nums1 +nums2:
            merged[k] += v
        
        return sorted(merged.items())