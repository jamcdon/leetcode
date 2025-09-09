#Count Valid Words from String

#Given a string and a list of valid letters, count how many words in the string can be formed using the letters in the valid letters list. For the input string, words are split using spaces. Punctuation and numbers are always considered valid letters. Both uppercase and lowercase are invalid for letters not present in the input list.

#Example:

#    Input:
#        String: "Hello, I am h2ere!"
#        Letters: "heloiar"
#    Output: 3
#    Explanation:
#        Valid words: "Hello,", "I", "h2ere!".
#        Invalid word: "am" (as 'm' is not present in the list of valid letters).
import re

def findValid(string: str, letters: str):
    string = string.lower()
    string = re.sub(r'[^a-z\s]', "", string)
    print(string)
    words = string.split(" ")

    total = 0
    for word in words:
        valid = True
        for letter in word:
            if letter not in letters:
                valid = False
                break
        if valid:
            total += 1
    return total

print(findValid("Hello, I am h2ere!", "heloiar"))
