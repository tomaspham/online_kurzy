
my_dictionary = {'Key': 'Value', ('K', 'E', 'Y'): 5}                # dictionaries have always curvy brackets
my_dictionary1 = {x: x + 1 for x in range(10)}

print(my_dictionary)
print(my_dictionary['Key'])                                         # prints value of the given key

print(my_dictionary1)

try:
    print(my_dictionary[1])
except Exception as e:
    print(e)

print(my_dictionary.keys())
print(my_dictionary.values())

my_dictionary[1] = 3                                                # adds to the dictionary [key] = value
del my_dictionary[1]                                                # deletes given key with its value
print(my_dictionary)

my_dictionary.clear()                                               # clears all dictionary / empty
print(my_dictionary)