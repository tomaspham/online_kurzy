
# <     less then
# >     greater than
# <=    less or equal to
# >=    greater or equal to
# !     not equal to
# ==    equal to

print(5 < 6)        # True


# sorted by power / priority
# not               # reverses the given boolean value
# and               # both conditions must be True
# or                # at least one condition must be True

a = True            # storing a boolean value to a variable
b = False           # storing a boolean value to a variable
print(not a)        # False
print( a and b)     # False
print(a or b)       # True


d = 5
e = 1
f = False
g = 'python'
h = 'some'
z = not((not(e <= d) and (g >= h)) or f) and 1      # when comparing strings the longer one is more powerfull
print(z)                                            # 1