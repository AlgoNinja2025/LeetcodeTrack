# Last updated: 7/21/2026, 7:07:43 PM
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        order = sorted(range(n), key=lambda i: positions[i])
        h = healths[:]
        alive = [True] * n
        stack = []
        
        for idx in order:
            if directions[idx] == 'R':
                stack.append(idx)
            else:  # left-moving robot
                while stack:
                    top = stack[-1]
                    
                    if h[top] < h[idx]:
                        # left robot wins
                        alive[top] = False
                        stack.pop()
                        h[idx] -= 1
                        # continue to next collision
                    elif h[top] > h[idx]:
                        # right robot wins
                        alive[idx] = False
                        h[top] -= 1
                        break  # left robot destroyed
                    else:
                        # equal health - both destroyed
                        alive[top] = False
                        alive[idx] = False
                        stack.pop()
                        break
        
        return [h[i] for i in range(n) if alive[i]]