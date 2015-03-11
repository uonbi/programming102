
#How to use enumarate()
#Trivial Example

#You have a list of programming languages:

langs = [['C++','C'],'Java','Ruby',
			'Python','Haskell','Hack','Rust',
			['JavaScript','ES6'],
			['Cobol','Scheme','Pascal','Basic','Scheme']]

#say you want to loop through and enumerate too
#notice I added some complexity with nested lists
#but never mind.

for i,j in enumerate(langs):
	print("Lang #",i,": ",j)

#i,j is a pair that's called a tuple - read on this!

