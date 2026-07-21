// Last updated: 7/21/2026, 7:07:42 PM
class Solution {
public:
    int minChanges(string s) {
        int c=0;
        char u=s[0];
        int total =0;

        for(int i=0;i<s.size();i++){
            if(u == s[i]) {c++;}
            else{
                if(c % 2 != 0){
                    total++;
                    c=0;
                }
                else{
                    c=1;
                    u=s[i];
                }
            }

        }
        return total;
    }
};