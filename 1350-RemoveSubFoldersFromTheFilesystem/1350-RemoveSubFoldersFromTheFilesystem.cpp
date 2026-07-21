// Last updated: 7/21/2026, 7:09:07 PM
class Solution {
public:
    vector<string> removeSubfolders(vector<string>& folder) {
        unordered_set<string> dirSet(folder.begin(), folder.end());
        vector<string> res;

        for (const string& dir : folder) {
            bool isSubfolder = false;
            for (int i = 1; i < dir.size(); i++) {
                if (dir[i] == '/' && dirSet.count(dir.substr(0, i))) {
                    isSubfolder = true;
                    break;
                }
            }
            if (!isSubfolder) {
                res.push_back(dir);
            }
        }

        return res;
    }
};
