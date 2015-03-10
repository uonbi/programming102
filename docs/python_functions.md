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

