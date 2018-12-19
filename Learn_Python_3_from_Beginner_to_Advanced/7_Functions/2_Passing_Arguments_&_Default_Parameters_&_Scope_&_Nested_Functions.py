
def parameters(a):                          # passing an argument to the function
    print(a)

parameters("This is a parameter")



def add(a,b):                               # passing 2 arguments to the function
    c = a + b
    return c

result = add(12,5)

print(result)



def add(a,b):
    c = a + b
    return c

result = add("One","word")

print(result)



def default_param(a,b = 4,c = 5):           # stating default parameters inside function arguments
    return a + b + c

result = default_param(3)

print(result)



def scope(a):
    a = a + 1
    print(a)
    return a

scope(5)



def outer(a):
    def nested(b):
        return b * a

    a = nested(a)
    return a

print(outer(4))



def f(a):
    def g(b):
        def h(c):
            return a * b * c
        return h
    return g

print(f(5)(2)(3))