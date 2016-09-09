
class Queue:
    """
    docstring for Queue

        * the first element in queue is at the start of list and will be dequeued first
        * FIFO
    """

    def __init__(self):
        # super(ClassName, self).__init__()
        self.items = []

    def is_empty(self):
        return (self.items == [])

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def dump(self):
        self.items = []

    def display(self):
        length = len(self.items)
        for i in range(0, length):
            print(self.items[i])

    def length(self):
        return len(self.items)


# build_queue()
t = int(raw_input())
for a0 in range(t):
    g = int(raw_input())
    for a1 in range(g):
        heads = 0
        arr = Queue()
        i, n, q = map(int, raw_input().split())
        if(i == 1):
            for j in range(n):
                arr.enqueue('H')
                heads += 1
            # now the Queue is filled
            for j in range(n):
                if(j % 2 == 0):
                    arr.enqueue('T')
                    arr.dequeue()
                    heads -= 1
                else:
                    arr.enqueue(arr.dequeue())
        # print heads
        else:
            for j in range(n):
                arr.enqueue('T')
            for j in range(n):
                if(j % 2 == 0):
                    arr.enqueue('H')
                    arr.dequeue()
                    heads += 1
                else:
                    arr.enqueue(arr.dequeue())
        if(q == 1):
            print heads
        else:
            print(n - heads)
