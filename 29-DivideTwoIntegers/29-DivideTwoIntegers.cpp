// Last updated: 7/21/2026, 7:10:21 PM
class Solution {
public:
    int divide(int dividend, int divisor) {
   if (divisor == 0) return INT_MAX; 
        
        // Edge case: Overflow condition (INT_MIN / -1 causes overflow)
        if (dividend == INT_MIN && divisor == -1) return INT_MAX;

        // Determine the sign of the quotient
        bool isNegative = (dividend < 0) ^ (divisor < 0);  

        // Convert both numbers to their absolute values to handle division correctly
        long long num = abs((long long)dividend);
        long long den = abs((long long)divisor);

        long long quotient = 0;

        // Subtraction method for division
        while (num >= den) {
            long long temp = den, multiple = 1;
            while (num >= (temp << 1)) { // Try to optimize using bit shifts
                temp <<= 1;
                multiple <<= 1;
            }
            num -= temp;
            quotient += multiple;
        }

        // Apply sign
        return isNegative ? -quotient : quotient;
    }
};