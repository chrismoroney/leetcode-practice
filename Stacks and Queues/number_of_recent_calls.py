# Number of Recent Calls

# You have a RecentCounter class which counts the number of recent requests within a certain time frame.

# Implement the RecentCounter class:

# RecentCounter() Initializes the counter with zero recent requests.
# int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, 
# and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). 
# Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].

# It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

from collections import deque

class RecentCounter(object):

    def __init__(self):
        self.q = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.q.append(t)

        while self.q[0] < t - 3000:
            self.q.popleft()

        return len(self.q)
        
if __name__ == "__main__":
    counter = RecentCounter()
    counter.ping(1)
    counter.ping(100)
    counter.ping(3001)
    counter.ping(3002)
    print(counter.ping(3003))


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)