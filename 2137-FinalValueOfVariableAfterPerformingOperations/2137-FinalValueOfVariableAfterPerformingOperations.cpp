// Last updated: 7/21/2026, 7:08:24 PM
class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int x=0;
        for(auto& op: operations)
            x+=(op[1]=='+')?1:-1;
        return x;
    }
};