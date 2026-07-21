// Last updated: 7/21/2026, 7:08:06 PM
class Solution {
public:
    int largestCombination(vector<int>& candidates) {
     int maxBit = 31;
    int maxCount = 0;

    for (int bit = 0; bit <= maxBit; ++bit) {
        int count = 0;
        for (int num : candidates) {
            if (num & (1 << bit)) {
                count++;
            }
        }
        maxCount = max(maxCount, count);
    }

    return maxCount;
    }
};