// Last updated: 7/21/2026, 7:09:05 PM
class Solution {
public:
    bool rotateString(string s, string goal) {
        string n = s + s;
        return( s.length() == goal.length() && n.find(goal) != string::npos);
    }
};