# Maximum Units on a Truck

# You are assigned to put some amount of boxes onto one truck. 
# You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

# numberOfBoxesi is the number of boxes of type i.
# numberOfUnitsPerBoxi is the number of units in each box of the type i.
# You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. 
# You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

# Return the maximum total number of units that can be put on the truck.

import heapq

class Solution(object):
    def maximum_units(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        max_heap = [(-units, box) for box, units in boxTypes]
        heapq.heapify(max_heap)

        answer = 0
        
        while truckSize > 0 and max_heap:
            num_units, num_boxes = heapq.heappop(max_heap)
            num_units *= -1

            boxes_to_load = min(num_boxes, truckSize)
            answer += boxes_to_load * num_units
            truckSize -= boxes_to_load
        
        return answer
    
if __name__ == "__main__":
    boxTypes = [[5,10],[2,5],[4,7],[3,9]]
    truckSize = 10
    sol = Solution()
    print(sol.maximum_units(boxTypes, truckSize))
