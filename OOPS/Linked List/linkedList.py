class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head
        self.last = head

    def isEmpty():
        return self.head == None

    def insertBeg(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

        if(self.last == None):
            self.last = new_node

    def insertEnd(self, data):
        new_node = Node(data)
        self.last.set_next(new_node)
        self.last = new_node

    def printList(self):
        temp = self.head
        while(temp != None):
            print temp.get_data()
            temp = temp.get_next()

    def size(self):
        temp = self.head
        counter = 0
        while(temp != None):
            counter += 1
            temp = temp.get_next()
        return counter

    def search(self, item):
        temp = self.head
        flag = False
        while(temp != None and not flag):
            if (temp.get_data() == item):
                flag = True
            temp = temp.get_next()
        return flag


l = LinkedList()
l.insertBeg(3)
l.insertBeg(2)
l.insertBeg(1)
l.insertBeg(0)
l.insertEnd(4)
l.insertEnd(5)
l.insertEnd(6)
l.printList()
print "size is : ", l.size()
print "found : ", l.search(9)
