int, float, string, set, tuple, list, dictionary, boolean, object, class, method, invocation, combination
+	- / // % ** ( ) != == and or not < <= > >= & | ^ ~ << >> . * [ ] [x][y] [start:stop:step] : , = operator combined equal operators
def main():
	body
if __name__	== "__main__": main()

Iteration

for x in range(start, stop, step):
for x in iterable object: (e.g. string, list, tuple, dictionary, list of list, dictionary of dictionary)

Branching

if	( ):
	if (	):
	elif ( ):
	else:
elif	( ):
else:
	
match (object):
	case (expr1):
	case (expr2):
... etc ...

Recursion

def recursive_function(parameters):
	base case 1
	base case x
	body
	recursive call
	recursive_function(state variable change, state variable change)

def function(parameter object vars):
	body
	return
	
Abstraction -> input x get y
Decomposition ->	Breaking up a task into smaller components, sub tasks

True, False, yield, lambda x:	x // 2, lambda x: x ** 2, lambda x:	L.append(f(x)), from x import y as z
break, continue, is, is not, in
assert, del, global, nonlocal, pass
try:
	body
except errorType:
	exception handling body
finally:
	clean-up
else:
	exception handling otherwise
	
IOError as e:
	e.method attribute
	
class Person(object):
	def __init__(self, name):
		self.name = name
		
	def __str__, def __repr__, operator overloading, def __gt__, def __ge__, def	__lt__, def __ne__ etc
	
magic methods

class Student(Person):
	def __init__(self, name, grades):
		super().__init__(name)
		self.grades = grades
		
Inheritance, Polymorphism

OO, UML

System Theory, Characteristic components (cases)	of building a system in Python

Standard Library

Modules

Examples for memorisation and interpretation intuitively and rules based (e.g. syntax, grammar, plausible structure)

Sockets, threading, program specification, urllib, scikit-learn, tensorflow, numpy, pandas, C/C++ OS API
Charles Truscott Watters 19th Aug 2022 Massachusetts Institute of Technology

	