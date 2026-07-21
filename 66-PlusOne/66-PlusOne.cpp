// Last updated: 7/21/2026, 7:10:01 PM
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int car =1;
        for(int i=digits.size()-1;i>=0;i--){
            int sum = car+digits[i];
            digits[i]=sum%10;
            car=sum/10;
        }
        if(car) digits.insert(digits.begin(),car);
        return digits;
    }
};