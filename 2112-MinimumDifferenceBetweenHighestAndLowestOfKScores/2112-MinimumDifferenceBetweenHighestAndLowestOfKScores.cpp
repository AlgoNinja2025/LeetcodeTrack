// Last updated: 7/21/2026, 7:08:30 PM
class Solution {
public:
    int minimumDifference(vector<int>& nums, int k) {
        if (k == 1) return 0;
        
        
        int n = nums.size();
        
        sort(nums.begin(), nums.end());
        
        int ans = INT_MAX;
        
       
        for (int i = 0; i <= n - k; i++) {
            int current_diff = nums[i + k - 1] - nums[i];
            ans = min(ans, current_diff);
        } 
        
        return ans;
    }
};