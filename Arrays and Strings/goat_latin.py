# Goat Latin

# You are given a string sentence that consist of words separated by spaces. Each word consists of lowercase and uppercase letters only.

# We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.) The rules of Goat Latin are as follows:

# If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to the end of the word.
# For example, the word "apple" becomes "applema".
# If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the end, then add "ma".
# For example, the word "goat" becomes "oatgma".
# Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
# For example, the first word gets "a" added to the end, the second word gets "aa" added to the end, and so on.
# Return the final sentence representing the conversion from sentence to Goat Latin.

class Solution(object):
    def to_goat_latin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        words = sentence.split(' ')
        new_words = []
        counter = 1

        for w in words:
            if w[0] not in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                c = w[0]
                w = w[1:] + c

            w += "ma"
            w += "a" * counter
            counter += 1
            new_words.append(w)

        return ' '.join(new_words)
    
if __name__ == "__main__":
    sentence = "The quick brown fox jumped over the lazy dog"
    sol = Solution()
    print(sol.to_goat_latin(sentence))