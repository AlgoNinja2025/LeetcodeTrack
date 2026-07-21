// Last updated: 7/21/2026, 7:06:46 PM
class Solution {
public:
    int minOperations(string s) {
        string trinovalex = s;  

        int maxSteps = 0;
        for (char c : trinovalex) {
            
            int steps = (26 + ('a' - c)) % 26;
            maxSteps = max(maxSteps, steps);
        }

        return maxSteps;
    }
};