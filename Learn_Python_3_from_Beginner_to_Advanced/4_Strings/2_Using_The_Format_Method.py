
print("Today I had {0} cups of {1}".format(3, "coffee"))                                # formats whatever is in curvy bracekts by given conditions
print('Prices: {x}, {y}, {z}'.format(x = 2.0, y = 1.5, z = 5))                          # can use single line variables
print("The {vehicle} had {0} crashes in {1} months".format(5, 6, vehicle = 'car'))      # using variables order in .format can be mixed

# {:<value}.format("string")                                                            # in order to alling text given value must be at least the length of the string
print('{:<20}'.format("text"))                                                          # allings text to the left (string length + number of spaces to move in a requested direction)
print('{:>20}'.format("text"))                                                          # allings text to the right (string length + number of spaces to move in a requested direction)


print('{:b}'.format(21))                                                                # 10101     # prints in binary
print('{:x}'.format(21))                                                                # 15        # prints in hex format
print('{:o}'.format(21))                                                                # 25        # prints in octal format
