"""
Keys and Rooms

There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. 
Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. 
Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, 
return true if you can visit all the rooms, or false otherwise.
"""

class Solution(object):
    def can_visit_all_rooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        seen = [False] * len(rooms)
        seen[0] = True

        stack = [0]

        while stack:
            keys = rooms[stack.pop()]

            for key in keys:
                if not seen[key]:
                    seen[key] = True
                    stack.append(key)

        return all(seen)
    

if __name__ == "__main__":
    # rooms = [[1,3],[3,0,1],[2],[0]]
    rooms = [[1],[2],[3],[]]
    sol = Solution()

    print(sol.can_visit_all_rooms(rooms))