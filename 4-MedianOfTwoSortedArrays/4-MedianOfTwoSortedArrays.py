# Last updated: 7/21/2026, 7:10:51 PM
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        

        n=sorted(nums1+nums2)
        l = len(n)
        mid = l//2
        return float(n[mid] if l%2 else (n[mid-1] + n[mid])/2.0) 
        