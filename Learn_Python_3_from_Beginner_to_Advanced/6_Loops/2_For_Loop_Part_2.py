
string = "String traversal!"

for i in range(len(string)):        # specifying the range by the length of the string
    print(string[i])                # spells out given string letter by letter


for char in string:                 # loops through the characters in the variable or given string
    print(char)                     # spells out given string letter by letter


for i in range(3):                  # this is executed 3 times
    for j in range(2):              # this can be either 0 or 1
        print(j)                    # 0 1 0 1 0 1 is printed

