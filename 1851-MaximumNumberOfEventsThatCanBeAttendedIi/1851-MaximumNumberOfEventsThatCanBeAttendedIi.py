# Last updated: 7/21/2026, 7:08:37 PM
import bisect

class Solution:
    def maxValue(self, events: list[list[int]], k: int) -> int:
        events.sort(key=lambda x: x[1])
        n = len(events)
        
        ends = [event[1] for event in events]
        
        
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            st, end, val = events[i - 1]
            for j in range(1, k + 1):
                
                dp[i][j] = dp[i - 1][j]
                
                p = bisect.bisect_right(ends, st - 1, hi=i - 1)
                dp[i][j] = max(dp[i][j], dp[p][j - 1] + val)
        
        return dp[n][k]
