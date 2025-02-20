'''
Smallest Number in Infinite Set

You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:

SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
int popSmallest() Removes and returns the smallest integer contained in the infinite set.
void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.
'''

import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.is_found = set()
        self.ints_added = []
        self.current_int = 1

    def popSmallest(self) -> int:
        if len(self.ints_added):
            num = heapq.heappop(self.ints_added)
            self.is_found.remove(num)
        else:
            num = self.current_int
            self.current_int += 1
        return num

    def addBack(self, num: int) -> None:
        if self.current_int <= num or num in self.is_found:
            return
        heapq.heappush(self.ints_added, num)
        self.is_found.add(num)

if __name__ == "__main__":
    sis = SmallestInfiniteSet()
    print(sis.addBack(2))    # 2 is already in the set, so no change is made.
    print(sis.popSmallest()) # return 1, since 1 is the smallest number, and remove it from the set.
    print(sis.popSmallest()) # return 2, and remove it from the set.
    print(sis.popSmallest()) # return 3, and remove it from the set.
    print(sis.addBack(1))    # 1 is added back to the set.
    print(sis.popSmallest())  # return 1, since 1 was added back to the set and is the smallest number, and remove it from the set.
    print(sis.popSmallest()) # return 4, and remove it from the set.
    print(sis.popSmallest()) # return 5, and remove it from the set.