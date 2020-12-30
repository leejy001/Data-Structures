class Node :
    def __init__(self, data):
        self.data = data
        self.llink = None
        self.rlink = None

    def __str__(self):
        return str(self.data)

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def __str__(self):
        node = self.front
        s_deque = '<=> '
        while True:
            s_deque += str(node)
            if node == self.rear:
                break
            try: node = node.rlink
            except: break
            s_deque += ', '
        s_deque += ' <=>'
        return s_deque

    def insertFront(self, data):
        new_node = Node(data)
        # 초기 상태일 때
        if self.front is None and self.rear is None:
            self.front = new_node
            self.front.rlink = self.rear
            self.rear = new_node
            self.rear.llink = self.front
        else:
            self.front.llink = new_node # 기존 front의 왼쪽 링크를 새노드로 변경
            new_node.rlink = self.front # 새노드의 오른쪽 링크를 기존 front로 변경
            self.front = new_node       # front를 새노드로 변경

    def insertRear(self, data):
        new_node = Node(data)
        # 초기 상태일 때
        if self.front is None and self.rear is None:
            self.front = new_node
            self.front.rlink = self.rear
            self.rear = new_node
            self.rear.llink = self.front
        else:
            self.rear.rlink = new_node  # 기존 rear의 오른쪽 링크를 새노드로 변경
            new_node.llink = self.rear  # 새노드의 왼쪽 링크를 기존 rear로 변경
            self.rear = new_node        # rear를 새노드로 변경

    def deleteFront(self):
        if self.isEmpty():
            return
        del_node = self.front
        value = del_node.data
        self.front = self.front.rlink   # 기존 front를 front의 오른쪽으로 변경
        del del_node                    # 기존 front 삭제
        return value

    def deleteRear(self):
        if self.isEmpty():
            return
        del_node = self.rear
        value = del_node.data
        self.rear = self.rear.llink     # 기존 rear를 rear의 왼쪽으로 변경
        del del_node                    # 기존 rear 삭제
        return value

    def peekFront(self):
        return self.front.data

    def peekRear(self):
        return self.rear.data

    def isEmpty(self):
        if self.front == self.rear:
            return True
        else:
            return False

if __name__ == "__main__":
    m_deque = Deque()
    m_deque.insertFront(3)
    m_deque.insertFront(2)
    m_deque.insertFront(1)
    print(m_deque)
    m_deque.insertRear(4)
    m_deque.insertRear(5)
    m_deque.insertRear(6)
    print(m_deque)
    print('Delete Front :', m_deque.deleteFront())
    print('Delete Rear :', m_deque.deleteRear())
    print('Delete Rear :', m_deque.deleteRear())
    print('Peek Rear   :', m_deque.peekRear())
    print(m_deque)