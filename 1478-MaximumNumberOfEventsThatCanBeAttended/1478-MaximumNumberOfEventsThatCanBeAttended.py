# Last updated: 7/21/2026, 7:08:47 PM
import heapq
class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        events.sort()

        n = len(events)
        attended_events = 0
        day = 0  
        event_idx = 0  
        min_heap = []  
        
        while event_idx < n or min_heap:
            if not min_heap and event_idx < n:
                day = max(day, events[event_idx][0])

            while event_idx < n and events[event_idx][0] <= day:
                heapq.heappush(min_heap, events[event_idx][1])
                event_idx += 1

            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            if min_heap:
                heapq.heappop(min_heap)
                attended_events += 1

            day += 1

        return attended_events