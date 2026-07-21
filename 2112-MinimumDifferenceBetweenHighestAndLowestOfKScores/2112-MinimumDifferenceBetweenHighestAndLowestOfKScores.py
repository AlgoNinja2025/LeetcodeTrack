# Last updated: 7/21/2026, 7:08:36 PM
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
       nums.sort()
       ans = float('inf')
       for i in range (len(nums)-k+1):
        cur_dif=nums[i+k-1]-nums[i]
        ans = min(ans,cur_dif)
       return ans 