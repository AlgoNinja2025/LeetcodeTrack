// Last updated: 7/21/2026, 7:10:00 PM
class Solution {
public:
    string addBinary(string a, string b) {
       int carry = 0;
        string result = ""; 
        int i = a.size() - 1;
        int j = b.size() - 1;
        while (i >= 0 || j >= 0 || carry > 0) {
            int sum = carry;
            if (i >= 0) {
                sum += a[i--] - '0';
            }
            if (j >= 0) {
                sum += b[j--] - '0';
            }
            carry = sum / 2;
            result = char(sum % 2 + '0') + result;
        }
        
        return result;
    }
};