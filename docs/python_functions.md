# Functions and Functional Programming

Substantial programs are broken up into functions for better modularity and ease of maintenance. Python makes it easy to define functions but also incorporates a surprising number of features from functional programming languages.

##Functions
Functions are defined with the def statement:

```python
def add(x,y):
	return x + y
```

The body of a function is simply a sequence of statements that execute when the function is called.You invoke a function by writing the function name followed by a tuple of function arguments, such as `a = add(3,4)`.

You can attach default arguments to function parameters by assigning values in the function definition. For example:

```python
def split(line,delimiter=','):
	statements
```

The use of mutable objects as default values may lead to unintended behavior:

```python
def foo(x, items=[]):
	items.append(x)
	return items

foo(1)
# returns [1]
foo(2)
# returns [1, 2]
foo(3)
# returns [1, 2, 3]
```

Notice how the default argument retains modifications made from previous invocations. To prevent this, it is better to use None and add a check as follows:

```python
def foo(x, items=None):
	if items is None:
		items = []
	items.append(x)
	return items
```

A function can accept a variable number of parameters if an asterisk(*) is added to the last parameter name.

To pass a tuple args to a function as if they were parameters, the *args syntax can be used in a function call as follows:

```python
def printf(fmt, *args):
	# Call another function and pass along args
	fprintf(sys.stdout, fmt, *args)
```

Function arguments can also be supplied by explicitly naming each parameter and specifying a value.These are known as keyword arguments. Here is an example:

```python
def foo(w,x,y,z):
	statements

# Keyword argument invocation
foo(x=3, y=22, w='hello', z=[1,2])
```


If the last argument of a function definition begins with ** , all the additional keyword arguments (those that don’t match any of the other parameter names) are placed in a dictionary and passed to the function.

You can combine extra keyword arguments with variable-length argument lists, as long as the ** parameter appears last:

```python
# Accept variable number of positional or keyword arguments
def spam(*args, **kwargs):
	# args is a tuple of positional args
	# kwargs is dictionary of keyword args
	...
```

## Parameter Passing and Return Values
When a function is invoked, the function parameters are simply names that refer to the passed input objects.The underlying semantics of parameter passing doesn’t neatly fit into any single style, such as “pass by value” or “pass by reference,” that you might know about from other programming languages. For example, if you pass an immutable value, the argument effectively looks like it was passed by value. However, if a mutable object (such as a list or dictionary) is passed to a function where it’s then modified, those changes will be reflected in the original object.

The `return` statement returns a value from a function. If no value is specified or you omit the return statement, the None object is returned.To return multiple values, place them in a tuple:

```python
def factor(a):
	d = 2
	while (d <= (a / 2)):
		if ((a / d) * d == a):
			return ((a / d), d)
		d = d + 1
	return (a, 1)
```

Multiple return values returned in a tuple can be assigned to individual variables:

```python
x, y = factor(1243) # Return values placed in x and y.

#OR

(x, y) = factor(1243) # Alternate version. Same behavior.
```

## Scoping Rules
Each time a function executes, a new **local namespace** is created.This namespace represents a local environment that contains the names of the function parameters, as well as the names of variables that are assigned inside the function body.When resolving names, the interpreter first searches the **local namespace**. If no match exists, it searches the **global namespace**. The global namespace for a function is always the *module* in which the function was defined. If the interpreter finds no match in the global namespace, it makes a final check in the **built-in namespace**. If this fails, a `NameError` exception is raised.

Variables in nested functions are bound using **lexical scoping**.That is, names are resolved by first checking the local scope and then all enclosing scopes of outer function definitions from the innermost scope to the outermost scope.

## Functions as Objects and Closures
Functions are first-class objects in Python.This means that they can be passed as arguments to other functions, placed in data structures, and returned by a function as a result. Example:

```
# foo.py
def callf(func):
	return func()
```

Here is an example using the above function:
```
>>> import foo
>>> def helloworld():
...		return 'Hello World'
...
>>> foo.callf(helloworld)
'Hello World'
```

When a function is handled as data, it implicitly carries information related to the surrounding environment where the function was defined. As an example, consider this modified version foo.py that now contains a variable definition:

```python
# foo.py
x = 42
def callf(func):
	return func()
```
Now, observe the behavior of this example:

```
>>> import foo
>>> x = 37
>>> def helloworld():
...		return "Hello World. x is %d" % x
...
>>> foo.callf(helloworld)
# Pass a function as an argument
'Hello World. x is 37'
```

In this example, notice how the function helloworld() uses the value of x that’s defined in the same environment as where helloworld() was defined.Thus, even though there is also an x defined in foo.py and that’s where helloworld() is actually
being called, that value of x is not the one that’s used when helloworld() executes.

When the statements that make up a function are packaged together with the environment in which they execute, the resulting object is known as a **closure**.

## Decorators
A decorator is a function whose primary purpose is to wrap another function or class. The primary purpose of this wrapping is to transparently alter or enhance the behavior of the object being wrapped. Syntactically, decorators are denoted using the special `@` symbol as follows:

```python
@trace
def square(x):
	return x*x
```

The preceding code is shorthand for the following:

```
def square(x):
	return x*x
square = trace(square)
```

## Generators and `yield`
If a function uses the `yield` keyword, it defines an object known as a generator. A generator is a function that produces a sequence of values for use in iteration. Here’s an example:

```python
def countdown(n):
	print("Counting down from %d" % n)
	while n > 0:
		yield n
	n -= 1
	return
```

If you call this function, you will find that none of its code starts executing. For example:

```
>>> c = countdown(10)
>>>
```

Instead, a generator object is returned. The generator object, in turn, executes the function whenever `next()` is called (or `__next__()` in Python 3). Here’s an example:

```
>>> c.next()				# Use c.__next__() in Python 3
Counting down from 10
10
>>> c.next()
9
```

You normally don’t call next() directly on a generator but use it with the `for` statement, `sum()`, or some other operation that consumes a sequence. For example:

```
for n in countdown(10):
	statements
a = sum(countdown(10))
```

## List Comprehensions
A common operation involving functions is that of applying a function to all of the items of a list, creating a new list with the results. For example:

```python
nums = [1, 2, 3, 4, 5]
squares = []

for n in nums:
	squares.append(n * n)
```

Because this type of operation is so common, it is has been turned into an operator known as a list comprehension. Here is a simple example:

```python
nums = [1, 2, 3, 4, 5]
squares = [n * n for n in nums]
```

The general syntax for a list comprehension is as follows:
```
[expression for item1 in iterable1 if condition1
			for item2 in iterable2 if condition2
			...
			for itemN in iterableN if conditionN ]
```

To illustrate, here are some more examples:

```
a = [-3,5,2,-10,7,8]
b = 'abc'

c = [2*s for s in a]			# c = [-6,10,4,-20,14,16]
d = [s for s in a if s >= 0]	# d = [5,2,7,8]
e = [(x,y) for x in a 			# e = [(5,'a'),(5,'b'),(5,'c'),
			for y in b 			# (2,'a'),(2,'b'),(2,'c'),
			if x > 0 ]			# (7,'a'),(7,'b'),(7,'c'),
								# (8,'a'),(8,'b'),(8,'c')]

f = [(1,2), (3,4), (5,6)]
g = [math.sqrt(x*x+y*y) 		# f = [2.23606, 5.0, 7.81024]
			for x,y in f]
```

## Generator Expression
A generator expression is an object that carries out the same computation as a list comprehension, but which iteratively produces the result.The syntax is the same as for list comprehensions except that you use parentheses instead of square brackets.


## The `lambda` Operator
Anonymous functions in the form of an expression can be created using the `lambda` statement:

```
lambda args : expression
```

`args` is a comma-separated list of arguments, and expression is an expression involving those arguments. Here’s an example:

```python
a = lambda x,y : x+y
r = a(2,3) 		# r gets 5
```

The primary use of lambda is in specifying short callback functions. For example, if you wanted to sort a list of names with case-insensitivity, you might write this:

```python
names.sort(key=lambda n: n.lower())
```

## Recursion
Recursive functions are easily defined. For example:

```python
def factorial(n):
	if n <= 1: return 1
	else: return n * factorial(n - 1)
```

However, be aware that there is a limit on the depth of recursive function calls. Python does not perform tail-recursion optimization that you often find in functional languages such as Scheme.

## Documentation Strings
It is common practice for the first statement of function to be a documentation string describing its usage. For example:

```python
def factorial(n):
	"""Computes n factorial. For example:
	>>> factorial(6)
	120
	>>>
	"""
	if n <= 1: return 1
	else: return n*factorial(n-1)
```

The documentation string is stored in the `__doc__` attribute of the function that is commonly used by IDEs to provide interactive help.


