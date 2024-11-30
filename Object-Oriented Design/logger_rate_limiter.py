# Logger Rate Limiter

# Design a logger system that receives a stream of messages along with their timestamps. 
# Each unique message should only be printed at most every 10 seconds (i.e. a message printed at timestamp t will prevent other identical messages from being printed until timestamp t + 10).

# All messages will come in chronological order. Several messages may arrive at the same timestamp.

# Implement the Logger class:

# Logger() Initializes the logger object.
# bool shouldPrintMessage(int timestamp, string message) Returns true if the message should be printed in the given timestamp, otherwise returns false.

class Logger(object):

    def __init__(self):
        self.message_map = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.message_map:
            self.message_map[message] = timestamp
            return True
        else:
            if timestamp >= self.message_map[message] + 10:
                self.message_map[message] = timestamp
                return True
        
        return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

if __name__ == "__main__":
    logger = Logger()
    print(logger.shouldPrintMessage(1, "foo"));  # return true, next allowed timestamp for "foo" is 1 + 10 = 11
    print(logger.shouldPrintMessage(2, "bar"));  # return true, next allowed timestamp for "bar" is 2 + 10 = 12
    print(logger.shouldPrintMessage(3, "foo"));  # 3 < 11, return false
    print(logger.shouldPrintMessage(8, "bar"));  # 8 < 12, return false
    print(logger.shouldPrintMessage(10, "foo")); # 10 < 11, return false
    print(logger.shouldPrintMessage(11, "foo")); # 11 >= 11, return true, next allowed timestamp for "foo" is 11 + 10 = 21