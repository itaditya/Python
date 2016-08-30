#!/usr/bin/env python3
from Queue import Queue


def build_queue(data_list):
    q = Queue()
    for data in data_list:
        q.enqueue(data)

    q.display()
    print(q.length())
    for i in range(1):
        # print(q.peek())
        q.enqueue(q.dequeue())

    q.display()


queue = build_queue([1, True, 2, 3])
