// Last updated: 7/21/2026, 7:07:45 PM
class Solution {
public:
    int maxMoves(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> dp(m, vector<int>(n, 0)); // DP table to store max moves

        int max_result = 0;

        // Traverse the grid from the second last column to the first
        for (int col = n - 2; col >= 0; --col) {
            for (int row = 0; row < m; ++row) {
                // Try moving to (row-1, col+1), (row, col+1), and (row+1, col+1)
                if (row > 0 && grid[row][col] < grid[row - 1][col + 1]) 
                    dp[row][col] = max(dp[row][col], 1 + dp[row - 1][col + 1]);
                
                if (grid[row][col] < grid[row][col + 1]) 
                    dp[row][col] = max(dp[row][col], 1 + dp[row][col + 1]);

                if (row + 1 < m && grid[row][col] < grid[row + 1][col + 1]) 
                    dp[row][col] = max(dp[row][col], 1 + dp[row + 1][col + 1]);
            }
        }

        // Check the maximum moves starting from any cell in the first column
        for (int i = 0; i < m; ++i) {
            max_result = max(max_result, dp[i][0]);
        }

        return max_result;
    }
};