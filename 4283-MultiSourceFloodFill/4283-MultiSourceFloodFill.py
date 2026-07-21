# Last updated: 7/21/2026, 7:06:45 PM
class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        grid=[[(-1,-1) for _ in range(m)] for _ in range(n)]
        queue=deque()

        for r,c,color in sources:
            grid[r][c]=(0,color)
            queue.append((r,c,0,color))


        directions=[(0,1),(0,-1),(1,0),(-1,0)]

        while queue:
            r,c,time,color=queue.popleft()

            for dr,dc in directions:
                nr,nc=r+dr,c+dc

                if 0<=nr<n and 0<=nc<m:
                    ntime,ncolor=grid[nr][nc]

                    if ntime ==-1:
                        grid[nr][nc]=(time+1,color)
                        queue.append((nr,nc,time+1,color))

                    elif ntime ==time+1:
                        if color > ncolor:
                            grid[nr][nc]=(time+1,color)
                            queue.append((nr,nc,time+1,color))

        return [[grid[r][c][1] for c in range(m)] for r in range(n)]