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

def rec_conv(binary, dec_no):
	next = dec_no // 2
	binary.push(dec_no%2)
	if (next != 0):
		rec_conv(binary,next)

def decToBinary(dec_no) :
	s = Stack()
	rec_conv(s, dec_no)
	# return s
	return "".join(map(str,s.items[::-1]))

dec_no = int(input("Enter A Decimal Number : "))
print(dec_no, "in Binary is ", decToBinary(dec_no))
