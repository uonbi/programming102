#Collection Data Types

##Tuples
* A tuple is an ordered sequence of zero or more object references.
* Tuples support the same slicing and striding syntax as strings.
* Like strings, tuples are immutable, so we cannot replace or delete any of their items. If we want to be able to modify an ordered sequence, we simply use a list instead of a tuple; or if we already have a tuple but want to modify it, we can convert it to a list using the list() conversion function and then apply the changes to the resultant list.