# Task Scheduler

# You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. 
# Each CPU interval can be idle or allow the completion of one task. 
# Tasks can be completed in any order, but there's a constraint: 
# there has to be a gap of at least n intervals between two tasks with the same label.

# Return the minimum number of CPU intervals required to complete all tasks.

import heapq

class Solution:
    def least_interval(self, tasks, n):
        freq_arr = [0] * 26
        for task in tasks:
            freq_arr[ord(task) - ord('A')] += 1

        pq = [-f for f in freq_arr if f > 0]
        heapq.heapify(pq)

        time = 0
        while pq:
            schedule = n
            count = 0
            group = []
            while pq and schedule >= 0:
                freq = -1 * heapq.heappop(pq)
                if freq > 1:
                    group.append(-1 * (freq - 1))
                count += 1
                schedule -= 1
            for item in group:
                heapq.heappush(pq, item)
            time += count if not pq else n + 1
        return time
        
if __name__ == "__main__":
    sol = Solution()
    tasks = ["A","A","A", "B","B","B"]
    n = 3
    print(sol.least_interval(tasks, n))
