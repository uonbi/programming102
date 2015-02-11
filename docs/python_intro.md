#Introduction to Python

##Creating and Running Python Programs
Python files normally have an extension of .py , although on some Unix-like system (e.g., Linux and Mac OS X) some Python applications have no extension, and Python GUI (Graphical User Interface) programs usually have an extension of .pyw particularly on Windows and Mac OS X.

In your home directory:

* Create a directory called `your-name`, and inside that directory create a sub-directory called `python` (that is where we will save all our Python files in this class)
* Create a file called hello.py in a plain text editor (*Sublime Text* or *GEdit* for our case), with the following content:

```python
#!/usr/bin/env python3
print("Hello", "World!")
```
* Save the file in `python` directory created earlier, as `hello.py`.

>The first line is a comment. In Python, comments begin with a # and continue to the end of the line.
>Each statement encountered in a .py file is executed in turn, starting with the first one and progressing line by line.

* Change directory (`cd`) to the `python` directory where we have `hello.py`
Python provides several built-in data types, but, i.e. `int` and `str`.

* To execute the program/file:

```bash
$ python3 hello.py
```

##Exploring Python

###Data Types
we will concern ourselves with only two of them for now, i.e. integers using the `int` type and strings using the `str` type.

Here are some of the examples of integer and string literals:

```python
-973
210624583337114373395836055367340864637790190801098222508621955072
0
"Infinitely Demanding"
'Simon Critchley'
'positively αβγ ÷© '
''
```

Incidentally, the second number shown is 2<sup>217</sup> — the size of Python’s integers is limited only by machine memory, not by a fixed number of bytes.

Strings can be delimited by double or single quotes, as long as the same kind are used at both ends, and since Python uses Unicode, strings are not limited to ASCII characters, as the penultimate string shows. An empty string is simply one with nothing between the delimiters.

Python uses square brackets (`[]`) to access an item from a sequence such as a string. 

For instance, go to the Python Shell and try out the following:
```
>>> "Programming 102"[3]
'g'
>>> "SCI"[0]
'S'
```
>**Note:** The Python Shell is accessed by simply typing `python3` on the terminal. 

In Python, both str and the basic numeric types such as int are *immutable* — that is, once set, their value cannot be changed.

To convert a data item from one type to another we can use the syntax datatype(item). For example:
```
>>> int("45")
45
>>> str(912)
'912'
```

The int() conversion is tolerant of leading and trailing whitespace, so int("  45  ") would have worked just as well.

###Object References (Variables)
Let’s look at a few tiny examples, and then discuss some of the details.
```python
x = "blue"
y = "green"
z = x
```

The syntax is simply `objectReference = value`. There is no need for predeclaration and no need to specify the value’s type.

The = operator is not the same as the variable assignment operator in some other languages. The = operator binds an object reference to an object in memory. If the object reference already exists, it is simply re-bound to refer to the object on the right of the = operator; if the object reference does not exist it is created by the = operator.

As noted earlier, comments begin with a `#` and continue until the end of the line:

```
print(x, y, z) #prints: blue green blue
x = y
print(x, y, z) #prints: blue green green
x = z
print(x, y, z) #prints: green green green
```

After the fourth statement (`x = z`), all the three object references are referring to the same `str`. Since there is no more object references to the "blue" string, Python is free to *garbage-collect* it.

The names used for object references (called *identifiers*) have a few restrictions:

* They may not be the same as any of Python's keywords
* Must start with a letter or an underscore and be followed by zero or more non-whitespace letter, underscore or digit characters.
* Python identifiers are case-sensitive, e.g. `LIMIT`, `Limit` and `limit` are three different identifiers.

Python uses **dynamic typing**, which means that an object reference can be re-bound to refer to a different object (which may be of a different data type) at any time. Languages that use *strong typing* (such as C, C++ and Java) allow only those operations that are defined for the data types involved to be performed. For example:

```
route = 866
print(route, type(route)) #prints: 866 <class 'int'>

route = "North"
print(route, type(route)) #prints: North <class 'str'>
```

The type() function returns the data type (also known as the “class”) of the data item it is given—this function can be very useful for testing and debugging.

###Collection Data Types
Python provides several collection data types that can hold items, including *associative arrays* and *sets*. But here we will introduce just two: *tuple* and *list*. Python tuples and
lists can be used to hold any number of data items of any data types.

Tuples are immutable, so once they are created we cannot change them. Lists are mutable, so we can easily insert items and remove items whenever we want.

Tuples are created using commas ( , ), as these examples show:
```
>>> "Denmark", "Finland", "Norway", "Sweden"
('Denmark', 'Finland', 'Norway', 'Sweden')
>>> "one",
('one',)
```

When Python outputs a tuple it encloses it in parentheses.

Here are some example lists:
```
[1, 4, 9, 16, 25, 36, 49]
['alpha', 'bravo', 'charlie', 'delta', 'echo']
['zebra', 49, -879, 'aardvark', 200]
[]
```

The fourth list shown is an empty list.

Like everything else in Python, collection data types are objects, so we can nest collection data types inside other collection data types, for example, to create lists of lists, without formality.

In procedural programming we call functions and often pass in data items as arguments. For example, we have already seen the print() function. Another frequently used Python function is len() , which takes a single data item as its argument and returns the “length” of the item as an int . Here are a few calls to len():

```
>>> len(("one",))
1
>>> len([3, 5, 1, 2, "pause", 5])
6
>>> len("automatically")
13
```

All Python data items are objects (also called instances) of a particular data type (also called a class). We will use the terms data type and class interchangeably.

One key difference between an object, and the plain items of data that some other languages provide, is that an object can have methods. For example, the list type has an append() method, so we can append an object to a list like this:
```
>>> x = ["zebra", 49, -879, "aardvark", 200]
>>> x.append("more")
>>> x
['zebra', 49, -879, 'aardvark', 200, 'more']
```

The `append()` method mutates, that is, changes, the original list.

>If you are unfamiliar with object-oriented programming this may seem a bit strange at first. For now, just accept that Python has conventional functions called like this: `functionName(arguments)` ; and methods which are called like this: `objectName.methodName(arguments)`. (Object-oriented programming is covered later).

The dot (“access attribute”) operator is used to access an object’s attributes.

The list type has many other methods, including insert() which is used to insert an item at a given index position, and remove() which removes an item at a given index position.

###Input/Output
To be able to write genuinely useful programs we must be able to read input—for example, from the user at the console, and from files—and produce output, either to the console or to files.

We have already briefly looked at `print()`. Python provides the built-in `input()` function to accept input from the user. This function takes an optional string argument (which it prints on the console); it then waits for the user to type in a response and to finish by pressing `Enter` (or `Return`).

###Creating and Calling Functions
Here is the general syntax for creating a function:
```
def functionName(arguments):
	suite
```

The arguments are optional and multiple arguments must be comma-separated.

Every Python function has a return value; this defaults to `None` unless we return from the function using the syntax `return value`, in which case value is returned.