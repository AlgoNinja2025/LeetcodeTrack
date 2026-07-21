# Last updated: 7/21/2026, 7:09:02 PM
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obSet = set()
        for (x, y) in obstacles:
            obSet.add((x, y))
        dir = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        x, y, dx, dy, face, maxD = (0, 0, 0, 1, 0, 0)
        for c in commands:
            if c == -2:
                face = (face + 1) & 3
                dx, dy = dir[face]
            elif c == -1:
                face = (face + 3) & 3
                dx, dy = dir[face]
            else:
                for _ in range(c):
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in obSet:
                        break
                    x, y = nx, ny
                maxD = max(maxD, x * x + y * y)
        return maxD