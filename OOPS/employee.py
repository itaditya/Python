#!/usr/bin/env python3
def GCD(m, n):
	rem = m % n
	if( rem == 0):
		return n
	else :
		return GCD(n, rem)
class Employee :
	"""
	docstring for Employee
	"""
	def __init__(self, num, den) :
		# super(ClassName, self).__init__()
		self.num = int(num)
		self.den = int(den)

		if (self.den == 0) :
			raise RuntimeError('Denominator ca\'nt be Zero')

	def __str__(self) :
		return str(self.num)+"/"+str(self.den) 

f1 = Employee(66, 2)
f2 = Employee(3, -2)

print (f2)
print (f1 <= f2)
print (f1 > f2)

print (f1 * f2)
print (f1 / f2)
print (f1 == f2)
print (f1 != f2)


