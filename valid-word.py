#Valid Word

#A word is considered valid if:

#    It contains a minimum of 3 characters.
#    It contains only digits (0-9), and English letters (uppercase and lowercase).
#    It includes at least one vowel.
#    It includes at least one consonant.

#You are given a string word.

#Return true if word is valid, otherwise, return false.

import re

class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) >= 3:
            vowels = {"a", "e", "i", "o", "u"}
            consonants = {"b", "c", "d", "f", "g", "h", "j", "k", }
            alphaNumeric = re.search("^[a-zA-Z0-9_.-]*$", word)
            if alphaNumeric:
                hasVowel = re.search("[AEIOUaeiou]", word)
                if hasVowel:
                    hasConsonant = re.search("[BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz]", word)
                    if hasConsonant:
                        return True
        return False

solution = Solution()

words = ["234Adas", "b3", "a3$e"]

for word in words:
    print(solution.isValid(word))
