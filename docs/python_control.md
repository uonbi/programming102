# Control Structures

## Conditional Execution

The `if, else,` and `elif` statements control conditional code execution.The general format of a conditional statement is as follows:

```
if expression:
	statements
elif expression:
	statements
elif expression:
	statements
	...
else:
	statements
```

## Loops and Iteration
You implement loops using the for and while statements. Here’s an example:

```
while expression:
	statements

for i in s:
	statements
```

The while statement executes statements until the associated expression evaluates to false.The for statement iterates over all the elements of s until no more elements are available.

When looping, it is sometimes useful to keep track of a numerical index in addition to the data values. Here’s an example:

```
i = 0
for x in s:
	statements
	i += 1
```
Python provides a built-in function, enumerate() , that can be used to simplify this code:
```
for i,x in enumerate(s):
	statements
```

`enumerate(s)` creates an iterator that simply returns a sequence of tuples `(0, s[0]),(1, s[1]), (2, s[2])`, and so on.


Using the `zip()` function, you can iterate in parallel over two or more sequences, e.g:
```
# s and t are two sequences
for x,y in zip(s,t):
	statements
```

`zip(s,t)` combines sequences s and t into a sequence of tuples `(s[0],t[0]),(s[1],t[1]),(s[2], t[2])`, and so forth, stopping with the shortest of the sequences.

To break out of a loop, use the `break` statement.

To jump to the next iteration of a loop (skipping the remainder of the loop body), use the `continue` statement.

## Exceptions
*Exceptions* indicate errors and break out of the normal control flow of a program.

The general format of the raise statement is `raise Exception([value])`, where `Exception` is the exception type and `value` is an optional value giving specific details about the exception. Here’s an example:
```
raise RuntimeError("Unrecoverable Error")
```

To catch an exception, use the `try` and `except` statements, as shown here:

```
try:
	f = open('foo')
except IOError as e:
	statements
```

To catch all exceptions except those related to program exit, use `Exception` like this:
```
try:
	do something
except Exception as e:
	error_log.write('An error occurred : %s\n' % e)
```

The `finally` statement defines a cleanup action for code contained in a try block. Here’s an example:

```
f = open('foo','r')
	try:
	# Do some stuff
	...
finally:
	f.close()
	# File closed regardless of what happened
```

The `finally` clause isn’t used to catch errors. Rather, it’s used to provide code that must always be executed, regardless of whether an error occurs.

