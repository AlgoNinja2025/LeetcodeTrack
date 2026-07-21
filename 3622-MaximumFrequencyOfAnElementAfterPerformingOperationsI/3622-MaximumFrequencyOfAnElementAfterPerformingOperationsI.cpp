// Last updated: 7/21/2026, 7:07:08 PM
class Solution {
public:
    int maxFrequency(vector<int>& nums, int k, int numOperations) {
        int maxi = *max_element(nums.begin(),nums.end());
        vector<int> actual_freq(maxi+1);
        vector<int> max_freq(maxi+2);
        for(auto it:nums){
            actual_freq[it]++;
            int lower = max(it-k,1);
            int higher = min(maxi,it+k);
            max_freq[lower]++;
            max_freq[higher+1]--;

        }
        for (int i=1;i<=maxi;i++){
            max_freq[i]+=max_freq[i-1];
        }
        int ans=0;
        for (int i=1;i<=maxi;i++){
            int temp = min(actual_freq[i]+numOperations,max_freq[i]);
            ans = max(ans,temp);
        }
        return ans;
    }
};