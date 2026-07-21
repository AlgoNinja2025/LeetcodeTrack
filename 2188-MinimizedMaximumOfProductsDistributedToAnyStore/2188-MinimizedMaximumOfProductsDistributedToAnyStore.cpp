// Last updated: 7/21/2026, 7:08:14 PM
class Solution {
public:
    int minimizedMaximum(int n, vector<int>& quantities) {
        int max_quantity = 0;
        for (int it : quantities) {
            max_quantity = std::max(max_quantity, it);
        }

        int l = 1;
        int r = max_quantity;
        int ans = 0;
        
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (possible(n, quantities, mid)) {
                ans = mid;
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return ans;
    }

private:
    bool possible(int n, const std::vector<int>& quantities, int value) {
        for (int quantity : quantities) {
            int required_stores = std::ceil(static_cast<float>(quantity) / value);
            n -= required_stores;
            if (n < 0) return false;
        }
        return true;
    }
};