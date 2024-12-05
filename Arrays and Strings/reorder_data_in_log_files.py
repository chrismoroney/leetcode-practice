# Reorder Data in Log Files

# You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

# There are two types of logs:

# Letter-logs: All words (except the identifier) consist of lowercase English letters.
# Digit-logs: All words (except the identifier) consist of digits.
# Reorder these logs so that:

# The letter-logs come before all digit-logs.
# The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
# The digit-logs maintain their relative ordering.
# Return the final order of the logs.

class Solution(object):
    def reorder_log_files(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """

        dig_logs = []
        let_logs = []

        for log in logs:
            contents = log.split(' ')
            if contents[1].isdigit():
                dig_logs.append(log)
            else:
                let_logs.append(log)

        return_logs = sorted(let_logs, key=lambda x: (x.split(" ", 1)[1], x.split(" ", 1)[0])) 
        
        for log in dig_logs:
           return_logs.append(log)

        return return_logs

if __name__ == "__main__":
    logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    sol = Solution()

    print(sol.reorder_log_files(logs))