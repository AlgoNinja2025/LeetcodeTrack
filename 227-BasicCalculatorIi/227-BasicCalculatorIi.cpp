// Last updated: 7/21/2026, 7:09:20 PM
class Solution {
public:
    int calculate(string s) {
        vector<int> stack;
        int num = 0;
        char sign = '+';

        for (int i = 0; i < s.length(); i++) {
            char ch = s[i];

            
            if (isdigit(ch)) {
                num = num * 10 + (ch - '0');
            }

            
            if ((!isdigit(ch) && ch != ' ') || i == s.length() - 1) {

                if (sign == '+') {
                    stack.push_back(num);
                }
                else if (sign == '-') {
                    stack.push_back(-num);
                }
                else if (sign == '*') {
                    int top = stack.back();
                    stack.pop_back();
                    stack.push_back(top * num);
                }
                else if (sign == '/') {
                    int top = stack.back();
                    stack.pop_back();
                    stack.push_back(top / num); 
                }

                sign = ch;
                num = 0;
            }
        }

        
        int result = 0;
        for (int x : stack) {
            result += x;
        }

        return result;
    }
};