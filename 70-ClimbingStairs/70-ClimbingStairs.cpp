// Last updated: 7/21/2026, 7:09:57 PM
class Solution {
public:
    int climbStairs(int n) {
        if (n<2){
            return n;
        }
        int a =1;
        int b =2;
        for(int i = 3;i<=n;i++){
            int temp = b;
            b=a+b;
            a = temp;
        }
        return b;
    }
};