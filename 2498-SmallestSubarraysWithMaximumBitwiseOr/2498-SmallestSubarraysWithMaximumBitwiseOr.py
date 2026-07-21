# Last updated: 7/21/2026, 7:08:00 PM
class Solution(object):
    def smallestSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1] * n
        bits = [-1] * 32
        
        for i in range(n-1, -1, -1):
            max_or = 0
           
            for b in range(32):
                if nums[i] & (1 << b):
                    bits[b] = i
                if bits[b] != -1:
                    max_or |= (1 << b)
            
            max_pos = i
            for b in range(32):
                if bits[b] != -1 and bits[b] > max_pos:
                    max_pos = bits[b]
            
            answer[i] = max_pos - i + 1
        
        return answer