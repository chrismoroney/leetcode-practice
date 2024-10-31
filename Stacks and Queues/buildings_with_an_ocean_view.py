# Buildings with an Ocean View

# There are n buildings in a line. 
# You are given an integer array heights of size n that represents the heights of the buildings in the line.

# The ocean is to the right of the buildings. 
# A building has an ocean view if the building can see the ocean without obstructions. 
#Formally, a building has an ocean view if all the buildings to its right have a smaller height.

# Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

class Solution(object):
    def find_buildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        n = len(heights)

        return_list = []
        stack = []

        for i in reversed(range(n)):
            while stack and heights[stack[-1]] < heights[i]:
                stack.pop()
            
            if not stack:
                return_list.append(i)
            
            stack.append(i)
        
        return_list.reverse()
        return return_list
    
if __name__ == "__main__":
    solution = Solution()
    heights = [4,2,3,1]
    print(solution.find_buildings(heights))