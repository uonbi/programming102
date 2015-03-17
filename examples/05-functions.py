
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