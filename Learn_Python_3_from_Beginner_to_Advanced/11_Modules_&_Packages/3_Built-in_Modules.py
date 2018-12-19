
'''

import copy

my_dictionary = {'key':'Value', ('K','E','Y'):5}
my_dictionary1 = copy.deepcopy(my_dictionary)
my_dictionary[1] = 1

print(my_dictionary)
print(my_dictionary1)

'''

import math as m
import cmath as cm
import random as ran
import sys

print(m.cos(m.pi))
print(m.ceil(1.6))


print(dir(cm))
print(cm.sqrt(4))
print(cm.polar(complex(0,1)))
print(dir(ran))


print(ran.random())
print(ran.randint(5,100))


print(sys.getrecursionlimit())

