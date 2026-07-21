// Last updated: 7/21/2026, 7:09:58 PM
int mySqrt(int x) {
   if (x == 0) {
        return 0;
    }

    int left = 1;
    int right = x;

    while (left <= right) {
        int mid = left + (right - left) / 2;
        long long square = (long long)mid * mid; // Ensure no integer overflow

        if (square == x) {
            return mid;
        } else if (square > x) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    return right;
}