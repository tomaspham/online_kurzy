
tup = (1, 'abc', 2, 'cde')                      # cannot change values in the tuples
tup1 = 3, 'efg', True

tup2 = 'A' #  tup2 = ('A',)
print(tup[0:2])

tup = tup[0:3] + (5,)
print(tup)
print(tup2 * 4)
print(5 in tup)                                 # is contained in the list/tup? boolean result


for x in ('a', 'b', 'c'):
    print(x)


def multiple_results():
    return (1,2,'a')

print(multiple_results())
print((1,2,3) == (1,2))