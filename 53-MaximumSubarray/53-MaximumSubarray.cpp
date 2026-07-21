// Last updated: 7/21/2026, 7:10:06 PM
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxsum = INT_MIN;
        //int maxsum = 0;
        int currentsum = 0;
        for(int num : nums){
            currentsum=max(num,currentsum+num);
            maxsum=max(maxsum,currentsum);

     
        }
        return maxsum;
    }
};