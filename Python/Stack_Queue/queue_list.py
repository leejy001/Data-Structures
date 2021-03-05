class ListQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if len(self.queue) == 0:
            return -1
        return self.queue.pop(0)

    def show(self):
        print(self.queue)

    def qsize(self):
        return len(self.queue)

if __name__=="__main__":
    lq = ListQueue()
    lq.enqueue(1)
    lq.enqueue(2)
    lq.enqueue(3)
    lq.enqueue(4)
    print('Queue Size() :', lq.qsize())
    lq.show()
    print('Dequeue :', lq.dequeue())
    print('Dequeue :', lq.dequeue())
    lq.show()