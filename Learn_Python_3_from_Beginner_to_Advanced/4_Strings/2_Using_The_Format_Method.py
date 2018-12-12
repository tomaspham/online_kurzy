
print(f"Today I had {3} cups of {'coffee'}")                                # formats whatever is in curvy bracekts by given conditions
print(f'Prices: {2.0}, {1.5}, {5}')                          # can use single line variables
print(f"The {'car'} had {5} crashes in {6} months")      # using variables order in .format can be mixed

# {:<value}.format("string")                                                            # in order to alling text given value must be at least the length of the string
print('{:<20}'.format("text"))                                                          # allings text to the left (string length + number of spaces to move in a requested direction)
print('{:>20}'.format("text"))                                                          # allings text to the right (string length + number of spaces to move in a requested direction)


print(f"{21:b}")
print('{:b}'.format(21))  # 10101     # prints in binary
print('{:x}'.format(21))                                                                # 15        # prints in hex format
print('{:o}'.format(21))                                                                # 25        # prints in octal format
