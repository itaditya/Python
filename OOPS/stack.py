#!/usr/bin/env python3
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

s = Stack()

print (s.is_empty())
s.push("First")
print (s.is_empty())
print (s.peek())
s.dump()
print (s.is_empty())
s.push(10000)
print (s.pop())
print (s.is_empty())
s.push(10000)
s.push("Fg")
s.push(True)
s.display()




