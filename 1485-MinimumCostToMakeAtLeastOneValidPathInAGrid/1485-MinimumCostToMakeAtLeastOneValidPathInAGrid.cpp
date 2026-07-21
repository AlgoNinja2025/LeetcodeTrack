// Last updated: 7/21/2026, 7:08:48 PM
class Solution {
public:
    int minCost(vector<vector<int>>& grid) {
    
         int m = grid.size();
        int n = grid[0].size();

        // Direction vectors corresponding to right, left, down, up
        vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        
        // Min-heap for the BFS with cost as priority
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> pq;
        vector<vector<int>> cost(m, vector<int>(n, INT_MAX));
        
        // Start from the top-left corner
        pq.push({0, 0, 0}); // {cost, row, col}
        cost[0][0] = 0;

        while (!pq.empty()) {
            auto [cur_cost, i, j] = pq.top();
            pq.pop();

            // If we've reached the bottom-right corner, return the cost
            if (i == m - 1 && j == n - 1) {
                return cur_cost;
            }

            // Explore all possible directions
            for (int dir = 0; dir < 4; ++dir) {
                int ni = i + directions[dir].first;
                int nj = j + directions[dir].second;

                // Check if the direction is within bounds
                if (ni >= 0 && ni < m && nj >= 0 && nj < n) {
                    int new_cost = cur_cost + (grid[i][j] != dir + 1); // Cost 1 if the sign is not matching
                    if (new_cost < cost[ni][nj]) {
                        cost[ni][nj] = new_cost;
                        pq.push({new_cost, ni, nj});
                    }
                }
            }
        }

        // If there's no valid path, return -1 (although the problem guarantees a path exists)
        return -1;
    }
};