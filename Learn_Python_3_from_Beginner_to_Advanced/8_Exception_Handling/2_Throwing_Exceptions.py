
a = 1

def RaiseException(a):
    if type(a) != type('a'):                                    # comparing pairs of data string types (boolean result)
        raise ValueError('This is not a string')

try:
    RaiseException(a)
except ValueError as e:
    print(e)



def TestCase(a,b):
    assert a < b, "a is greater than b"

try:
    TestCase(2,1)

except  AssertionError as e:
    print(e)