# Moving Average from Data Stream

# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

# Implement the MovingAverage class:

# MovingAverage(int size) Initializes the object with the size of the window size.
# double next(int val) Returns the moving average of the last size values of the stream.

from collections import deque

class MovingAverage(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.size = size
        self.queue = deque()
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        size, queue = self.size, self.queue

        queue.append(val)
        if len(queue) > size:
            queue.popleft()

        return float(sum(queue)) / min(len(queue), size)
        

if __name__ == "__main__":
    size = 3
    obj = MovingAverage(size)
    print(obj.next(1))
    print(obj.next(10))
    print(obj.next(3))
    print(obj.next(5))
