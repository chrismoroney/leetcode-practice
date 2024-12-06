class Solution(object):
    def first_uniq_char(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s:
            return -1

        map_of_chars = {}

        for i in range(len(s)):
            if s[i] not in map_of_chars:
                map_of_chars[s[i]] = 1
            else:
                map_of_chars[s[i]] += 1

        for i in range(len(s)):
            if map_of_chars[s[i]] == 1:
                return i
        return -1
    
if __name__ == "__main__":
    sol = Solution()
    s = "loveleetcode"
    print(sol.first_uniq_char(s))
