// Last updated: 7/21/2026, 7:09:13 PM
struct Cell {
    int x, y, height;
    Cell(int x, int y, int height) : x(x), y(y), height(height) {}
    bool operator>(const Cell& other) const {
        return height > other.height;
    }
};
class Solution {
public:
    int trapRainWater(vector<vector<int>>& heightMap) {
        if (heightMap.empty() || heightMap[0].empty()) return 0;

    int m = heightMap.size(), n = heightMap[0].size();
    priority_queue<Cell, vector<Cell>, greater<Cell>> minHeap;
    vector<vector<bool>> visited(m, vector<bool>(n, false));

    // Add all boundary cells to the min-heap and mark them as visited
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (i == 0 || j == 0 || i == m - 1 || j == n - 1) {
                minHeap.push(Cell(i, j, heightMap[i][j]));
                visited[i][j] = true;
            }
        }
    }

    // Directions for moving to the 4 neighboring cells (up, down, left, right)
    vector<int> directions = {-1, 0, 1, 0, -1};

    int trappedWater = 0;

    // Process the min-heap
    while (!minHeap.empty()) {
        Cell current = minHeap.top();
        minHeap.pop();

        // Check all 4 neighboring cells
        for (int i = 0; i < 4; ++i) {
            int newX = current.x + directions[i];
            int newY = current.y + directions[i + 1];

            // Ensure the new cell is within bounds and has not been visited
            if (newX >= 0 && newX < m && newY >= 0 && newY < n && !visited[newX][newY]) {
                // If the neighboring cell is lower, water will be trapped
                if (heightMap[newX][newY] < current.height) {
                    trappedWater += current.height - heightMap[newX][newY];
                }

                // Push the neighbor to the heap with the maximum height between the current cell and the neighbor
                minHeap.push(Cell(newX, newY, max(heightMap[newX][newY], current.height)));
                visited[newX][newY] = true;
            }
        }
    }

    return trappedWater;
    }
};