
list = [1, 'abc', (2,3)]                    # lists always in square brackets

print(list)

print(list[2])

print(list[2][0])                           # index at a given index

print(list + ['4'])

print(list * 2)

print(2 in list)

print(list == [1, 'abc', (2,3)])

print(list[:2])

list.append(6)                              # adds element at the end of the list

list[len(list):] = [7]

print(list)