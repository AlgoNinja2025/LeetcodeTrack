// Last updated: 7/21/2026, 7:10:49 PM
class Solution {
public:
    string longestPalindrome(string s) {
        int ans=0,n=s.size();
        string st="";
        for(int i=0;i<n;i++){
            int l=i,r=i;
            while(l>=0 && r<n && s[l]==s[r]){
                int len=r-l+1;
                if(len>ans){
                    ans=len;
                    st=s.substr(l,len);
                }
                l--;
                r++;

            }
            l=i;
            r=i+1;
            while(l>=0 && r<n && s[l]==s[r]){
                int len = r-l+1;
                if(len>ans){
                    ans=len;
                    st=s.substr(l,len);
                }
                l--;
                r++;
            }
        }
        return st;
        
    }
};