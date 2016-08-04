#!/usr/bin/env python3
# Check how to import class from other files , till then
class Queue :
	"""
	docstring for Queue

	    * the first element in queue is at the start of list and will be dequeued first
	    * FIFO
	"""
	def __init__(self) :
		# super(ClassName, self).__init__()
		self.items = []

	def is_empty(self) :
		return (self.items == [])

	def enqueue(self, item) :
		self.items.append(item)

	def dequeue(self) :
		return self.items.pop(0)

	def peek(self) :
		return self.items[0]

	def dump(self) :
		self.items = []

	def display(self) :
		length = len(self.items)
		for i in range(0,length):
			print (self.items[i])

	def length(self) :
		return len(self.items)

def build_queue(data_list) :
	q = Queue()
	for data in data_list:
		q.enqueue(data)
	
	q.display()
	print(q.length())
	for i in range(1):
		# print(q.peek())
		q.enqueue(q.dequeue())	

	q.display()


queue = build_queue([1,True,2,3])
