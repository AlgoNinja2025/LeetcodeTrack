// Last updated: 7/21/2026, 7:10:44 PM
bool isPalindrome(int x) {
    if (x < 0 || (x % 10 == 0 && x != 0)) {
        return false;
    }

    int r, temp = x, sum = 0;
    while (x != 0) {
        r = x % 10;
        if (sum > INT_MAX / 10 || (sum == INT_MAX / 10 && r > 7)) {
            return false; 
        }
        sum = (sum * 10) + r;
        x = x / 10;
    }
    return temp == sum;
}