#!/usr/bin/env python3


# Check how to import class from other files , till then
class Stack :
	"""
	docstring for Stack

	    * the top element is at the last of list
	"""
	def __init__(self) :
		# super(ClassName, self).__init__()
		self.items = []

	def is_empty(self) :
		return (self.items == [])

	def push(self, item) :
		self.items.append(item)

	def pop(self) :
		return self.items.pop()

	def peek(self) :
		return self.items[len(self.items)-1]

	def dump(self) :
		self.items = []

	def display(self) :
		length = len(self.items)
		print ("\t",self.items[length-1],"<--")
		for i in range(1,length):
			print ("\t",self.items[length-i-1])

	def length(self) :
		return len(self.items)

def par_checker(symbol_string) :
	s = Stack()
	balanced = True
	index = 0

	while index < len(symbol_string) and balanced :
		symbol = symbol_string[index]
		if symbol == "(" :
			s.push(symbol)
		else :
			# that is ) bracket
			if (s.is_empty()):
				# checked whether ) is left alone 
				balanced = False 
			else :
				s.pop()
		index += 1

	if balanced and s.is_empty():
		return True
	else :
		return False

print(par_checker("(((((())))"))
print(par_checker("(())"))
