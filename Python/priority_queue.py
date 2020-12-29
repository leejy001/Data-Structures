class Node:
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return f'{self.data}'

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        new_node = Node(element)
        self.queue.append(new_node)

    def dequeue(self):
        entry = 0
        # 우선순위 결정 값이 낮은 순서대로 빠져나감
        for i in range(len(self.queue)):
            if self.queue[i].data < self.queue[entry].data:
                entry = i
        return self.queue.pop(entry)

    def show(self):
        for node in self.queue:
            print(node.data, end=' ')
        print()

    def qsize(self):
        return len(self.queue)

if __name__=="__main__":
    lq = PriorityQueue()
    lq.enqueue(7)
    lq.enqueue(4)
    lq.enqueue(1)
    lq.enqueue(3)
    print('Queue Size() :', lq.qsize())
    lq.show()
    print('Dequeue :', lq.dequeue())
    print('Dequeue :', lq.dequeue())
    lq.show()