# Merge Intervals

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort(key=lambda x: x[0])

        return_list = []
        for interval in intervals:
            n = len(return_list)
            if not return_list or return_list[-1][1] < interval[0]:
                return_list.append(interval)
            else:
                return_list[-1][1] = max(return_list[-1][1], interval[1])
        
        return return_list
        
if __name__ == "__main__":
    sol = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(sol.merge(intervals))