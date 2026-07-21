// Last updated: 7/21/2026, 7:09:08 PM
class Solution {
public:
    bool judgeCircle(string moves) {
        int x = 0, y = 0;

        for (int i = 0; i < moves.length(); i++) {
            char move = moves[i];

            if (move == 'U') {
                y += 1;
            }
            else if (move == 'D') {
                y -= 1;
            }
            else if (move == 'L') {
                x -= 1;
            }
            else if (move == 'R') {
                x += 1;
            }
        }

        return (x == 0 && y == 0);
    }
};