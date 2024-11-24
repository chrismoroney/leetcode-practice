# Reorganize String

# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

# Return any possible rearrangement of s or return "" if not possible.

from collections import Counter
import heapq

class Solution(object):
    def reorganize_string(self, s):
        """
        :type s: str
        :rtype: str
        """
        return_arr = []

        pq = [(-freq, c) for c, freq in Counter(s).items()]
        heapq.heapify(pq)

        while pq:
            first_freq, first_c = heapq.heappop(pq)
            if not return_arr or first_c != return_arr[-1]:
                return_arr.append(first_c)
                if first_freq + 1 != 0:
                    heapq.heappush(pq, (first_freq + 1, first_c))
            else:
                if not pq:
                    return ""
                second_freq, second_c = heapq.heappop(pq)
                return_arr.append(second_c)
                if second_freq + 1 != 0:
                    heapq.heappush(pq, (second_freq + 1, second_c))
                heapq.heappush(pq, (first_freq, first_c))
            
        return ''.join(return_arr)
        
if __name__ == "__main__":
    sol = Solution()
    s0 = "aaaabbbccd"
    s1 = "aaaaab"
    print(sol.reorganize_string(s0))
    print(sol.reorganize_string(s1))