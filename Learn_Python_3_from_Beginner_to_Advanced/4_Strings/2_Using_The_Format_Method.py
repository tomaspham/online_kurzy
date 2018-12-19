
print("Today I had {0} cups of {1}".format(3, "coffee"))                                # formats whatever is in curvy bracekts by given conditions
print(f"Today I had {3} cups of {'coffee'}")                                            # the same as the previous one but with different sintax

print('Prices: {x}, {y}, {z}'.format(x = 2.0, y = 1.5, z = 5))                          # can use single line variables
print(f'Prices: {2.0}, {1.5}, {5}')                                                     # the same as the previous one but with different sintax

print("The {vehicle} had {0} crashes in {1} months".format(5, 6, vehicle = 'car'))      # using variables order in .format can be mixed
print(f"The {'car'} had {5} crashes in {6} months")                                     # the same as the previous one but with different sintax


# {:<value}.format("string")                                                            # in order to alling text given value must be at least the length of the string
print('{:<20}'.format("text"))                                                          # allings text to the left (string length + number of spaces to move in a requested direction)
print(f'{"text":<20}')                                                                  # the same as the previous one but with different sintax

print('{:>20}'.format("text"))                                                          # allings text to the right (string length + number of spaces to move in a requested direction)
print(f'{"text":>20}')                                                                  # the same as the previous one but with different sintax


print('{:b}'.format(21))                                                                # 10101     # prints in binary
print(f'{21:b}')                                                                        # the same as the previous one but with different sintax

print('{:x}'.format(21))                                                                # 15        # prints in hex format
print(f'{21:x}')                                                                        # the same as the previous one but with different sintax

print('{:o}'.format(21))                                                                # 25        # prints in octal format
print(f'{21:o}')                                                                        # the same as the previous one but with different sintax