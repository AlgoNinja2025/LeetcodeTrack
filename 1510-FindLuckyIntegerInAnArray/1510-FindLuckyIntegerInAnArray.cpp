// Last updated: 7/21/2026, 7:08:54 PM
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <iostream>

class Solution {
public:
    int findLucky(std::vector<int>& arr) {
        std::unordered_map<int, int> counts;

       
        for (int num : arr) { 
            counts[num]++;
        }

        int largestLucky = -1;

        
        for (auto const& [num, count] : counts) { 
            if (num == count) { 
                largestLucky = std::max(largestLucky, num); 
            }
        }

        return largestLucky;
    }
};