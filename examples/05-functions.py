
def foo(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items

def factor(a):
    d = 2
    while (d <= (a / 2)):
        if ((a / d) * d == a):
            return ((a / d), d)
        d = d + 1
    return (a, 1)

#Decorators
@trace
def square(x):
    return x*x

def square(x):
    return x*x
square = trace(square)

#Yield
def countdown(n):
    print("Counting down from %d" % n)
    while n > 0:
        yield n
    n -= 1
    return

for n in countdown(10):
    statements
a = sum(countdown(10))

#Lambda
a = lambda x,y : x+y
r = a(2,3)

#Recursion
def factorial(n):
    if n <= 1: return 1
    else: return n * factorial(n - 1)

#Look for other recursion examples:
