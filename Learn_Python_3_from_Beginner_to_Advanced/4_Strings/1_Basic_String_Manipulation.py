
string = 'I am string in Python'        # storing a string to a variable
string1 = " I am string in Python"      # storing a string to a variable

print(string[5:11])                     # string    # prints whatever is in the index range of x to y (y not included)
print(string[:4])                       # I am      # prints everything up to index 5 (5 not included)
print(string[15:])                      # Python    # prints everything after index 15 (15 included)


# string[-1] = 'x'                      # TypeError: 'str' object does not support item assignment
print(len('My length is 15'))           # 15        # prints the length of the given string (not including 0)
print(len(string))                      # 21        # prints the length of the given string from variable (not including 0)
print(string[-1])                       # n         # prints out the letter at the given index from the back (first index is 1 not 0)


string2 = 'Con' + 'catenation'          # adding strings together in a variable
string2 = 'Con' 'catenation'            # + sign is not necessary
print(string2)                          # Concatenation

string2 = 2 * ('Con' + 'catenation')    # adding strings together and repeating them by by given number
print(string2)                          # ConcatenationConcatenation


con = 'Con'                             # storing a string to a variable
cat = 'catenate'                        # storing a string to a variable
print(con + cat)                        # Concatenate
                                        # when adding strings together from multiple variables + sign must connect them
print(con + 'catenate')                 # Concatenate


word = "Ford"                           # storing a string to a variable
word = 'L' + word[1:]                   # changing a stored value by adding given string + string from the variable before excecution
print(word)                             # Lord