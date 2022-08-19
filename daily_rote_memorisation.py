int, float, string, set, tuple, list, dictionary, boolean, method, class, object, invocation, combination
x = 1993
y = 2.718
z = "Charles Truscott"
L	= [lambda x: ((2 *	(x ** 2) / 2, lambda x: ((3 *	(x ** 2)) / 3)]
val = True
also_val = False
also_also_val = val or also val
also_also_val -> True

and ->	True if both are true
or ->	True if any are true
not -> False if true, true if false

x.next() type
class Object(object)
x = return_primes_up_to(100000)
x = [{0: lambda y: x *	y for x in range(0, 100, 1)}]

+ - *	/ // % ** (	)	!= == and, or, not > >= < <=, & | ^	~ <<	>>	. *	[::] [ ][ ] , =, assignment operator combinations also e.g. +=, <<= >>= , &=

for x in range(start, stop, step):
for q in iterable type:	(e.g. list, tuple, string, dictionary)

def recursive_function(param_one, param_two):
	base case 1:
	base case 2:
	base case x:
	body
	recursive call
	recursive_function(param_two, param_one - param_two)

if (Boolean):
	if(Boolean):
		if(Boolean):
		elif (Boolean):
		elif (Boolean)
		else:
	else:
else:
	
etc

match (object):
	case condition:
... etc ...

def main():
	body
	
def function(parameters):
	body
	return
	
operators and operands

data and method attributes

program specification

Object-Oriented Programming vs. Procedural Programming

Higher-order programming, function pointers

Searching and sorting: exhaustive enumeration, bisection search, newton-raphson, bubble sort, permutation sort, selection sort, merge sort

class Fraction(object):
	def __init__(self, numerator, denominator):
		self.numerator = numerator
		self.denominator = denominator
	def __str__, def __gt__, def __repr__ etc
	def add(self, other):
		if type(other)	!= Fraction:
			return
		new_numerator = self.numerator *	other.denominator + self.denominator *	other.numerator
		new_denominator = self.denominator *	other.denominator
	etc, multiply, divide, reciprocal, subtract
	
class Decimal(Fraction):
	def __init__(self, decimal_val)
		numerator = super().numerator
		denominator = super().denominator
		self.decimal_val = float(self.numerator / self.denominator)
bad code

True, False, lambda, yield, from x import y as z
break, continue, is, is not, in
try:
	body
except	ErrorType as e:
finally:
	do something
else:
	body
	
decomposition, abstraction

Program specification
Characteristics of building a software system, requirements analysis

Python standard library including wintypes windll and kernel32.dll, mscvrt.dll

Charles Truscott Watters MIT	22