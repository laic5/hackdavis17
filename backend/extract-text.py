import re
from nltk import tokenize

with open('alice/chp1.txt', 'r') as myfile:
    input_string = myfile.readlines()

print(str(input_string[0:2]))
