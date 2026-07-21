# Last updated: 7/21/2026, 7:08:03 PM
class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        
        
        available_rooms = [r for r in range(n)]
        heapq.heapify(available_rooms)

        
        
        occupied_rooms = []

        
        booking_counts = [0] * n

        
        meetings.sort()

        for start_time, end_time in meetings:
            
            
            while occupied_rooms and occupied_rooms[0][0] <= start_time:
                
                
                free_time, room_num = heapq.heappop(occupied_rooms)
                heapq.heappush(available_rooms, room_num)

            if available_rooms:
                
                room_to_assign = heapq.heappop(available_rooms)
                
                heapq.heappush(occupied_rooms, [end_time, room_to_assign])
            else:
                
                
                free_time, room_to_assign = heapq.heappop(occupied_rooms)
                
                
                new_end_time = free_time + (end_time - start_time)
                
                heapq.heappush(occupied_rooms, [new_end_time, room_to_assign])

            
            booking_counts[room_to_assign] += 1

        
        
        max_bookings = -1
        most_booked_room = -1
        for i in range(n):
            if booking_counts[i] > max_bookings:
                max_bookings = booking_counts[i]
                most_booked_room = i
        return most_booked_room
