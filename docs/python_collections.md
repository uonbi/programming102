#Collection Data Types / Sequence Types

*Sequences* represent ordered sets of objects indexed by non-negative integers and include strings, lists, and tuples. 

Strings are sequences of characters, and lists and tuples are sequences of arbitrary Python objects. Strings and tuples are immutable; lists allow insertion, deletion, and substitution of elements. All sequences support iteration.

##Operations Common to All Sequence Types

Item | Description
:------------------ |: -------------------------------
`s [i]` | Returns element `i` of a sequence
`s [ i :j]` | Returns a slice
`s[i:j:stride]` | Returns an extended slice
`len(s)` | Number of elements in `s`
`min(s)` | Minimum value in `s`
`max(s)` | Maximum value in `s`
`sum(s [,initial])` | Sum of items in `s`
`all(s)` | Checks whether all items in `s` are `True`.
`any(s)` | Checks whether any item in `s` is `True`.

<br/>

##Operations Applicable to Mutable Sequences
Item | Description
:-------------------- |:----------------------------
`s[i] = v` | Item assignment
`s[i:j] = t` | Slice assignment
`s[i:j:stride] = t` | Extended slice assignment
`del s[i]` | Item deletion
`del s[i:j]` | Slice deletion
`del s[i:j:stride]` | Extended slice deletion

<br/>

## Brief Overview of the Collection Types

###Lists
The built-in function `list(s)` converts any iterable type to a list. If s is already a list, this function constructs a new list that’s a shallow copy of s .

Check manuals for various list operations like .append(), .count(), .pop(), .remove(), .sort(), .reverse(), etc.

###Mapping Types
Dictionaries are the only built-in mapping type and are Python’s version of a hash table or associative array.You can use any immutable object as a dictionary key value (strings, numbers, tuples, and so on). Lists, dictionaries, and tuples containing mutable objects cannot be used as keys (the dictionary type requires key values to remain constant).

###Set Types
A set is an unordered collection of unique items. Unlike sequences, sets provide no indexing or slicing operations.They are also unlike dictionaries in that there are no key values associated with the objects.The items placed into a set must be immutable.Two different set types are available: `set` is a mutable set, and `frozenset` is an immutable set.






