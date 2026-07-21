// Last updated: 7/21/2026, 7:10:08 PM
class Solution {
public:
    bool isValid(vector<string>&tmp,int row,int col){
        int tmpRow=row,tmpCol=col;
        while(row>0){
            row--;
            if(tmp[row][col]=='Q')return false;
        }
        row=tmpRow;col=tmpCol;
        while(row>0 && col>0){
            row--;col--;
            if(tmp[row][col]=='Q')return false;
        }
        row=tmpRow;col=tmpCol;
        while(row>0 && col<tmp[0].size()){
            row--;col++;
            if(tmp[row][col]=='Q')return false;
        }
        return true;
    }
    void solve(vector<vector<string>>&ans,vector<string>&tmp,int &n,int r){
        if(r==n){
            ans.push_back(tmp);
            return;
        }
        for(int i=0;i<n;i++){
            if(isValid(tmp,r,i)){
                tmp[r][i]='Q';
                solve(ans,tmp,n,r+1);
                tmp[r][i]='.';
            }
        }
    }
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>>ans;
        vector<string>tmp(n,string(n,'.'));
        solve(ans,tmp,n,0);
        return ans;
    }
};