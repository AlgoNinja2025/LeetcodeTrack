// Last updated: 7/21/2026, 7:09:55 PM
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int i;
        int n=nums.size();
        for(i=1;i<n;i++){
            int temp=nums[i];
            int j=i-1;

            while(j>=0 && nums[j]>temp){
                nums[j+1]=nums[j];
                j--;

            }

            nums[j+1]=temp;
        }

        //return nums;
    }
};