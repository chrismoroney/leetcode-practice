# Valid Word Abbreviation

# A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. 
# The lengths should not have leading zeros.

# For example, a string such as "substitution" could be abbreviated as (but not limited to):

# "s10n" ("s ubstitutio n")
# "sub4u4" ("sub stit u tion")
# "12" ("substitution")
# "su3i1u2on" ("su bst i t u ti on")
# "substitution" (no substrings replaced)
# The following are not valid abbreviations:

# "s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
# "s010n" (has leading zeros)
# "s0ubstitution" (replaces an empty substring)
# Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

# A substring is a contiguous non-empty sequence of characters within a string.

class Solution(object):
    def valid_word_abbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i = 0
        j = 0
        while i < len(word) and j < len(abbr):
            # is an char, needs to match letter of word
            if abbr[j].isalpha():
                if abbr[j] != word[i]:
                    return False
                i += 1
                j += 1
            # is a num, in which we need to find how many chars in word go with this num
            else:
                # leading 0's
                if abbr[j] == '0':
                    return False
                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                # do this to match the num to the length of abbr
                i += num
            
        return j == len(abbr) and i == len(word)
    
if __name__ == "__main__":
    sol = Solution()
    # returns True
    word = "antidisestablishmentarianism"
    abbr = "ant15n3ia4"
    print(sol.valid_word_abbreviation(word, abbr))

    # returns False
    word = "internationalization"
    abbr = "i12iz10n"
    print(sol.valid_word_abbreviation(word, abbr))