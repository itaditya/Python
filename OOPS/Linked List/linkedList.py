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
        if self.last == None:
            self.last = new_node
            self.head = new_node
        else:
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

    def delete(self, item):
        # current = self.head
        # ahead = self.head.get_next()
        # if(ahead == None):
        #     # only one element
        #     self.head = None
        # else:
        #     while(ahead != None):
        #         if (ahead.get_data() == item):
        #             break
        #         current = ahead
        #         ahead = ahead.get_next()
        #     current.set_next(ahead.get_next())
        #     # thus on coming out of loop we have current at the node just before
        #     # the toBeDeleted element and current at that element
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

a = LinkedList()
a.insertEnd(0)
a.insertEnd(1)
a.printList()
print "size is : ", a.size()
print "found : ", a.search(0)
print "deleted : "
a.delete(1)
print "found : ", a.search(0)
print "size is : ", a.size()
a.printList()
