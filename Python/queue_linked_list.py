class Node:
    def __init__(self, data):
        self.data = data
        self.link = None
    def __str__(self):
        return str(self.data)

class Queue:
    def __init__(self, data):
        new_node = Node(data)
        self.front = new_node
        self.rear = new_node
        self.front.link = self.rear     # front에서 rear로 링크 연결

    def __str__(self):
        s_queue = '<-'
        node = self.front
        while True:
            s_queue += str(node)
            if node is self.rear:
                break
            node = node.link
            s_queue += ', '
        s_queue += '<-'
        return s_queue

    def isEmpty(self):
        if self.front is self.rear:
            return True
        else:
            return False

    # 원소 삽입
    def enQueue(self, data):
        new_node = Node(data)
        self.rear.link = new_node
        # 삽입 시 rear를 새노드로 변경
        self.rear = new_node

    # 원소 삭제
    def deQueue(self):
        if not self.isEmpty():
            node = self.front
            value = node.data
            # front를 다음으로 옮기며 기존 프론트는 삭제
            self.front = self.front.link
            del node
            return value

    # front와 rear가 같을 때 남은 값 출력
    def peek(self):
        return self.front.data

if __name__=="__main__":
    m_queue = Queue(3)
    m_queue.enQueue(6)
    m_queue.enQueue(7)
    print(m_queue)
    print('deQueue :', m_queue.deQueue())
    print('deQueue :', m_queue.deQueue())
    print('deQueue :', m_queue.deQueue())
    print('   peek :', m_queue.peek())
    m_queue.enQueue(1)
    m_queue.enQueue(2)
    m_queue.enQueue(4)
    print(m_queue)
    print('deQueue :', m_queue.deQueue())