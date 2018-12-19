
my_set = {'one', 'two', 'three', 'one'}             # sets always in curvy brackets

print(my_set)

my_set1 = {'two', 'three', 'four'}

print(my_set1 | my_set)
print(my_set.union(my_set1))

print(my_set1 ^ my_set)
print(my_set.symmetric_difference(my_set1))

print(my_set1 - my_set)
print(my_set.difference(my_set1))
print(my_set1.difference(my_set))

a = my_set1 - my_set

print(a <= my_set)
print(a <= my_set1)

my_set.add('five')

print(my_set)