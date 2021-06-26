#program for all the cases which can check a string contains only a certain set of characters ( a-z, A-Z and 0-9).
import re
def char(string):
    charre = re.compile(r'[^A-Za-z0-9.]')
    string = charre.search(string)
    return not bool(string)

print(char("ABFKJHGFHdfukhudsafuhf656889692"))
print(char("%&^&**(%%$$*&%@#!}{"))

#program that matches a word containing ab.

import re
def Word(text):
        patterns = '\w*ab.\w*'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(Word("Have a good day."))
print(Word("He is absolutely fine."))

#A Python program to check for a number at the end of a word/sentence.
import re
def Word(text):
        patterns = '\w+\r*$'
        if re.search(patterns,text):
                return 'Found a match!'
        else:
                return('Not matched!')

print( Word("Have a good day"))
print( Word("Python is easy to learn."))
print( Word("Python is easy to learn "))

# Python program to search the numbers (0-9) of length between 1 to 3 in a given string

import re
results = re.finditer(r"([0-9]{1,3})", "Exercises number 1, 12, 13, and 345 are important")
print("Number of length 1 to 3")
for n in results:
     print(n.group(0))
     
#Python program to match a string that contains only uppercase letters

import re
def text_match(text):
        patterns = '^[a-zA-Z0-9_]*$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("Python is easy to learn"))
print(text_match("Python_Bootcamp"))
