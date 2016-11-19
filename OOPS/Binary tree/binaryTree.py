class Node(object):

    def __init__(self, data=None):
        self.data = data
        self.child_node_1 = None
        self.child_node_2 = None

    def get_data(self):
        return self.data

    def get_child_node_1(self):
        return self.child_node_1

    def get_child_node_2(self):
        return self.child_node_2

    def set_child_node_1(self, new_child_node_1):
        self.child_node_1 = new_child_node_1

    def set_child_node_2(self, new_child_node_2):
        self.child_node_2 = new_child_node_2


class binaryTree(object):

    def __init__(self, head=None):
        self.head = head
        self.latest = None

    def isEmpty(self):
        return self.head == None

    def insert(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
        else:
            if data < self.latest.get_data():
                self.latest.set_child_node_1(new_node)
            else:
                self.latest.set_child_node_2(new_node)
        self.latest = new_node

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

a = binaryTree()
print a.isEmpty()
a.insert(0)
a.insert(1)
a.insert(2)
print a.head.get_data()
print a.latest.get_data()

# a.insertEnd(1)
# a.printList()
# print "size is : ", a.size()
# print "found : ", a.search(0)
# print "deleted : "
# a.delete(1)
# print "found : ", a.search(0)
# print "size is : ", a.size()
# a.printList()
