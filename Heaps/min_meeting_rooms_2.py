# Problem: Minimum Meeting Rooms
# Given an array of meeting time intervals intervals where intervals[i] = [start_i, end_i], determine the minimum number of meeting rooms required.

import heapq

class Solution():
    def min_meeting_rooms(self, intervals):
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[0])

        heap = []

        heapq.heappush(heap, intervals[0][1])

        for i in range(1, len(intervals)):
            if intervals[i][0] >= heap[0]:
                heapq.heappop(heap)
            
            heapq.heappush(heap, intervals[i][1])

        return len(heap)
    
if __name__ == "__main__":
    solution = Solution()
    intervals = [[0, 30], [5, 10], [15, 20]]
    print(solution.min_meeting_rooms(intervals))