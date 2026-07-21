// Last updated: 7/21/2026, 7:10:52 PM
#
class Solution {
public:
    int lengthOfLongestSubstring(std::string s) {
        int n = s.length();
        int maxlen = 0;
        std::unordered_set<char> cset;
        int l = 0;

        for(int r = 0; r < n; r++) {
            if(cset.count(s[r]) == 0) {
                cset.insert(s[r]);
                maxlen = std::max(maxlen, r - l + 1);
            } else {
                while(cset.count(s[r])) {
                    cset.erase(s[l]);
                    l++;
                }
                cset.insert(s[r]);
            }
        }
        return maxlen;
    }
};