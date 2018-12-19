
# map()           # one is func other is sequence

print(list(map(lambda x: x**2 + 3 * x + 1, [1,2,3,4])))

print(list(filter(lambda x: x < 4, [1,2,3,4,5,4,3,2,1])))


import functools

print(functools.reduce(lambda x,y: x * y, [1,2,3,4]))
