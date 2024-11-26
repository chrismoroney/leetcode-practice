# Interval List Intersections

# You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. 
# Each list of intervals is pairwise disjoint and in sorted order.

# Return the intersection of these two interval lists.

# A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

# The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. 
# For example, the intersection of [1, 3] and [2, 4] is [2, 3].

class Solution(object):
    def interval_intersection(self, first_list, second_list):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """

        return_list = []
        i, j = 0, 0
        
        while i < len(first_list) and j < len(second_list):
            intersect_low = max(first_list[i][0], second_list[j][0])
            intersect_high = min(first_list[i][1], second_list[j][1])

            if intersect_low <= intersect_high:
                return_list.append([intersect_low, intersect_high])
            
            if first_list[i][1] < second_list[j][1]:
                i += 1
            else:
                j += 1

        return return_list

if __name__ == "__main__":
    sol = Solution()
    first_list = [[0,2],[5,10],[13,23],[24,25]]
    second_list = [[1,5],[8,12],[15,24],[25,26]]

    print(sol.interval_intersection(first_list, second_list))

# Examples
# [.   ]
#.   [.   ]

#.      [.  ]
#  [.     ]


# [.   ]
#.     [.    ]

# [.   ]
#.        [.    ]
