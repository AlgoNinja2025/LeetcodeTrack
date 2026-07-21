// Last updated: 7/21/2026, 7:08:56 PM
class Solution {
public:
    string makeFancyString(string s) {
        if (s.length() <= 2) {
            return s;
        }
        
        
        string result = "";
        
        
        for (int i = 0; i < s.length(); i++) {
            
            char currentChar = s[i];
            
           if (result.length() >= 2 && 
                result[result.length() - 1] == currentChar && 
                result[result.length() - 2] == currentChar) {
                
                continue;
            }
            
            
            result += currentChar;
        }
        
        return result;
    }
};