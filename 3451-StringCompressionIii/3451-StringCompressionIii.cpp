// Last updated: 7/21/2026, 7:07:29 PM
class Solution {
public:
    string compressedString(string word) {
         int n =word.size();
        string comp="";
        int count=1;
      
        for(int i =0 ;i<n-1;i++){
            if(word[i]!=word[i+1]){
                comp.push_back(count+'0');
                comp.push_back(word[i]);
                count=1;
            }else{
                count++;
                if(count==10){ 
                    comp.push_back(count-1+'0');
                    comp.push_back(word[i]);
                    
                    count=1;
                }
            }
        }
        
        comp.push_back(count+'0');
        comp.push_back(word[n-1]);
        return comp;
    }
};