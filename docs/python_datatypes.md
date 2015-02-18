#Data Types

##Identifiers and Keywords
Rules of naming identifiers:

* The start character can be anything that Unicode considers to be a letter, including the ASCII letters (“a”, “b”, ..., “z”, “A”, “B”, ..., “Z”), the underscore (“_”), as well as the letters from most non-English languages.
* Each continuation character can becany character that is permitted as a start character, or pretty well any non-whitespace character, including any character that Unicode considers to be a digit, such as (“0”, “1”, ..., “9”).
* Identifiers are case-sensitive, so for example, TAXRATE, Taxrate, TaxRate, taxRate, and taxrate are five different identifiers.
* No identifier can have the same name as one of Python’s keywords. For a complete list of Built-ins, run `dir(__builtins__)` on the Python Shell
* The use of underscores ( _ ): Names that begin and end with two underscores (such as `__lt__`) should not be used. Python defines various special methods and variables that use such names, but we should not introduce new names of this kind ourselves.

##Integers
* The size of an integer is limited only by the machine’s memory.
* Numeric operators and functions:

Syntax | Description
:-------------------------|:--------------------------
`x + y` | Adds number x and number y
`x - y` | Subtracts y from x
`x * y` | Multiplies x by y
`x / y` | Divides x by y ; always produces a float (or a complex if x or y is complex)
`x // y` | Divides x by y ; truncates any fractional part so always produces an int result; see also the round() function
`x % y` | Produces the modulus (remainder) of dividing x by y
`x ** y` | Raises x to the power of y ; see also the pow() functions
`abs(x)` | Returns the absolute value of x `divmod(x, y) | Returns the quotient and remainder of dividing x by y as a tuple of two int s
`pow(x, y)` | Raises x to the power of y ; the same as the ** operator
`pow(x, y, z)` | A faster alternative to (x ** y) % z
`round(x, n)` | Returns x rounded to n integral digits if n is a negative int or returns x rounded to n decimal places if n is a positive int.
`bin(i)` | Returns the binary representation of int i as a string, e.g., bin(1980) == '0b11110111100'
`hex(i)` | Returns the hexadecimal representation of i as a string, e.g. `hex(1980) == '0x7bc'`
`int(x)` | Converts object x to an integer
`int(s, base)` | Converts str s to an integer. If the optional base argument is given it should be an integer between 2 and 36 inclusive.
`oct(i)` | `Returns the octal representation of i as a string`

 <br/>

* Integer literals are written using base 10 (decimal) by default, but other
number bases can be used when this is convenient. Binary numbers are written with a leading `0b` , octal numbers with a leading `0o`, and hexadecimal numbers with a leading `0x`. Uppercase letters can also be used.

* While for float s, the round() function works in the expected way—for example, round(1.246, 2) produces 1.25 —for int s, using a positive rounding value has no effect and results in the same number being returned, since there are no decimal digits to work on. But when a negative rounding value is used a subtle and useful behavior is achieved—for example, round(13579, -3) produces 14000 , and round(34.8, -1) produces 30.0.

* All the binary numeric operators ( `+ , - , / , // , % ,` and `**` ) have augmented assignment versions ( `+= , -= , /= , //= , %= ,` and `**=` ) where `x op= y` is logically equivalent to `x = x op y`.


## Boolean
* There are two built-in Boolean objects: `True` and `False`.

* Python provides three logical operators: `and` , `or` , and `not`. Both `and` and `or` use short-circuit logic and return the operand that determined the result, whereas `not` always returns either `True` or `False`.


## Floating-Point Types

* Python provides three kinds of floating-point values: the built-in `float` and
`complex` types, and the `decimal.Decimal` type from the standard library.

* Numbers of type `float` are written with a decimal point, or using exponential
notation, for example, `0.0, 4., 5.7, -2.5, -2e9, 8.9e-4`.

* Computers natively represent floating-point numbers using base 2—this means that some decimals can be represented exactly (such as 0.5), but others only approximately (such as 0.1 and 0.2). Furthermore, the representation uses a fixed number of bits, so there is a limit to the number of digits that can be held. Example:

```
>>> 0.0, 5.4, -2.5, 8.9e-4
(0.0, 5.4000000000000004, -2.5, 0.00088999999999999995)
```

* Floating-point numbers can be converted to integers using the `int()` function which returns the whole part and throws away the fractional part, or using `round()` which accounts for the fractional part, or using `math.floor()` or `math.ceil()` which convert down to or up to the nearest integer. The `float.is_integer()` method returns `True` if a floating-point number’s fractional part is 0, and a float’s fractional representation can be obtained using the `float.as_integer_ratio()` method. For example, given `x = 2.75`, the call `x.as_integer_ratio()` returns `(11, 4)`. Integers can be converted to floating point numbers using `float()`.

## Decimal Numbers

* In many applications the numerical inaccuracies that can occur when using floats don’t matter, and in any case are far outweighed by the speed of calculation that float s offer. But in some cases we prefer the opposite trade-off, and want complete accuracy, even at the cost of speed. 

* The decimal module provides immutable Decimal numbers that are as accurate as we specify. Calculations involving Decimal s are slower than those involving float s, but whether this is noticeable will depend on the application.

* To create a Decimal we must import the decimal module. For example:

```
>>> import decimal
>>> a = decimal.Decimal(9876)
>>> b = decimal.Decimal("54321.012345678987654321")
>>> a + b
Decimal('64197.012345678987654321')
```

## Strings

* String literals are created using quotes &mdash; single, double or triple quotes. Examples:

```python
text = """A triple quoted string like this can include 'quotes' and
"quotes" without formality. We can also escape newlines \
so this particular string is actually only two lines long."""
```

* If we want to write a long string literal spread over two or more lines but without using a triple quoted string there are a couple of approaches we can take:

```python
t = "This is not the best way to join two long strings " + \
"together since it relies on ugly newline escaping"
s = ("This is the nice way to join two long strings "
"together; it relies on string literal concatenation.")
```

### Slicing and Striding Strings

* individual characters in a string, can be extracted using the item access operator(`[]`)

* The slice operator has three syntaxes:
```
seq[start]
seq[start:end]
seq[start:end:step]
```
The first syntax, it extracts the start-th item from the sequence. The second syntax extracts a slice from and including the start-th item, up to and excluding the end-th item.

>*Tip:* You can reverse a string with e.g. `x[::-1]`

### String Operators and Methods

* Membership testing with `in`
* Concatenation with `+`
* Appending with `+=`
* Replication with `*`
* Augmented assignment replication with `*=`
* `len()` returns the length / number of characters in a string, 0 for an empty string.
* In cases where we want to concatenate lots of strings the `str.join()` method offers a better solution (than `+`). he method takes a sequence as an argument (e.g., a list or tuple of strings), and joins them together into a single string with the string the method was called on between each one. For example:

```
>>> treatises = ["Arithmetica", "Conics", "Elements"]
>>> " ".join(treatises)
'Arithmetica Conics Elements'
>>> "-<>-".join(treatises)
'Arithmetica-<>-Conics-<>-Elements'
>>> "".join(treatises)
'ArithmeticaConicsElements'
```

* The `str.join()` method can also be used with the built-in `reversed()` function, to reverse a string, for example, `"".join(reversed(s))`, although the same result can be achieved more concisely by striding, for example, `s[::-1]`.

* In cases where we want to find the position of one string inside another, we
have two methods to choose from. One is the `str.index()` method; this returns
the index position of the substring, or raises a `ValueError` exception on failure. The other is the `str.find()` method; this returns the index position of the sub-string, or `-1` on failure.

* Other String methods worth noting: *s.capitalize(), s.count(t,start,end), s.endswith(x,start,end), s.replace(t,u,n), s.startswith(x,start,end), s.strip(chars), s.lower(), s.upper()* &mdash; there are numerous others, check reference.

### String Formatting with the str.format() Method
* The str.format() method returns a new string with the replacement fields in
its string replaced with its arguments suitably formatted. For example:

```
>>> "The novel '{0}' was published in {1}".format("Hard Times", 1854)
"The novel 'Hard Times' was published in 1854"
```

* Using Filed names
```
>>> "{who} turned {age} this year".format(who="She", age=88)
'She turned 88 this year'
```

```
>>> stock = ["paper", "envelopes", "notepads", "pens", "paper clips"]
>>> "We have {0[1]} and {0[2]} in stock".format(stock)
'We have envelopes and notepads in stock'
```

```
>>> d = dict(animal="elephant", weight=12000)
>>> "The {0[animal]} weighs {0[weight]}kg".format(d)
'The elephant weighs 12000kg'
```

###Format Specifications

Examples:
```
>>> "{0:25}".format(s)
# minimum width 25
'The sword of truth
'
>>> "{0:>25}".format(s) # right align, minimum width 25
'The sword of truth'
>>> "{0:^25}".format(s) # center align, minimum width 25
'The sword of truth'
>>> "{0:-^25}".format(s) # - fill, center align, minimum width 25
'---The sword of truth----'
>>> "{0:.<25}".format(s) # . fill, left align, minimum width 25
'The sword of truth.......'
>>> "{0:.10}".format(s) # maximum width 10
'The sword '
```





