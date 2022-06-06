# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word):
    # [assignment] Add your code here
    length = len(word)
    if word == word[::-1]:
        return True
    else:
        return False

a = print(find_anagrams('hello'))