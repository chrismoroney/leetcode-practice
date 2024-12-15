# Design a data structure that accepts a stream of integers and checks if it has a pair of integers 
# that sum up to a particular value.

# Implement the TwoSum class:

# TwoSum() Initializes the TwoSum object, with an empty array initially.
# void add(int number) Adds number to the data structure.
# boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, 
# otherwise, it returns false.

class TwoSum(object):

    def __init__(self):
        self.map_num = {}

    def add(self, number):
        """
        :type number: int
        :rtype: None
        """
        if number not in self.map_num:
            self.map_num[number] = 1
        else:
            self.map_num[number] += 1
        

    def find(self, value):
        """
        :type value: int
        :rtype: bool
        """

        for key in self.map_num.keys():
            diff = value - key
            
            if key != diff:
                if diff in self.map_num:
                    return True
            
            elif self.map_num[key] > 1:
                return True

        return False


if __name__ == "__main__":
    twosum = TwoSum()
    twosum.add(1)
    twosum.add(2)
    twosum.add(3)
    twosum.add(4)
    twosum.add(5)
    twosum.add(6)
    twosum.add(7)
    twosum.add(8)
    print(twosum.find(100))
    print(twosum.find(13))