#!/usr/bin/env python3
def GCD(m, n):
	rem = m % n
	if( rem == 0):
		return n
	else :
		return GCD(n, rem)
class Fraction :
	"""
	docstring for Fraction
	"""
	def __init__(self, num, den) :
		# super(ClassName, self).__init__()
		self.num = int(num)
		self.den = int(den)

		if (self.den < 0) :
			self.num *= -1
			self.den *= -1

		if (self.den == 0) :
			raise RuntimeError('Denominator ca\'nt be Zero')

	def __str__(self) :
		return str(self.num)+"/"+str(self.den) 

	def __add__(self, fract_2) :
		new_num = self.num*fract_2.den + self.den*fract_2.num
		new_den = self.den * fract_2.den
		common = GCD(new_num, new_den)
		return Fraction(new_num//common,new_den//common)

	def __sub__(self, fract_2) :
		new_num = self.num*fract_2.den - self.den*fract_2.num
		new_den = self.den * fract_2.den
		common = GCD(new_num, new_den)
		return Fraction(new_num//common,new_den//common)

	def __mul__(self, fract_2) :
		new_num = self.num * fract_2.num
		new_den = self.den * fract_2.den
		common = GCD(new_num, new_den)
		return Fraction(new_num//common,new_den//common)

	def __truediv__(self, fract_2) :
		new_num = self.num * fract_2.den
		new_den = self.den * fract_2.num
		common = GCD(new_num, new_den)
		return Fraction(new_num//common,new_den//common)

	def __eq__(self, fract_2) :
		# Denominator is made same and num is checked
		return ((self.num*fract_2.den) == (fract_2.num*self.den))

	def __le__(self, fract_2) :
		# Denominator is made same and num is checked
		return ((self.num*fract_2.den) <= (fract_2.num*self.den))

	def __ge__(self, fract_2) :
		# Denominator is made same and num is checked
		return ((self.num*fract_2.den) >= (fract_2.num*self.den))

	def __lt__(self, fract_2) :
		# Denominator is made same and num is checked
		return ((self.num*fract_2.den) < (fract_2.num*self.den))

	def __gt__(self, fract_2) :
		# Denominator is made same and num is checked
		return ((self.num*fract_2.den) > (fract_2.num*self.den))

	def __ne__(self, fract_2) :
		# Denominator is made same and num is checked
		return ((self.num*fract_2.den) != (fract_2.num*self.den))

f1 = Fraction(66, 2)
f2 = Fraction(3, -2)

print (f2)
print (f1 <= f2)
print (f1 > f2)

print (f1 * f2)
print (f1 / f2)
print (f1 == f2)
print (f1 != f2)


