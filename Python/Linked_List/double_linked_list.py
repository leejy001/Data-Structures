class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None    # 이전 링크 추가

    def __str__(self):
        return str(self.data)

class DoubleLinkedList:
    def __init__(self, data):
        new_node = Node(data)
        self.head = new_node
        self.list_size = 1

    def __str__(self):
        s_list = ''
        node = self.head
        while True:
            s_list += str(node)
            if node.next == self.head:
                break
            node = node.next
            s_list += '<->'
        return s_list

    # 처음 노드 삽입
    def insertFirst(self, data):
        new_node = Node(data)
        if self.head.prev is not None:
            new_node.prev = self.head.prev
            self.head.prev.next = new_node
        if self.head.next is not None:
            new_node.next = self.head.next
        self.head.prev = new_node
        self.head = new_node

    # 중간 노드 삽입 (앞)
    def insertMiddleBefore(self, idx, data):
        node = self.selectNode(idx)
        new_node = Node(data)
        new_node.prev = node.prev
        new_node.next = node
        node.prev.next = new_node
        node.prev = new_node
        self.list_size += 1

    # 중간 노드 삽입 (뒤)
    def insertMiddleAfter(self, idx, data):
        node = self.selectNode(idx)
        new_node = Node(data)
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node
        self.list_size += 1

    # 마지막 노드 삽입
    def insertLast(self, data):
        new_node = Node(data)
        if self.head.next is None:
            self.head.next = new_node
            new_node.prev = self.head
        if self.head.prev is not None:
            self.head.prev.next = new_node
            new_node.prev = self.head.prev
        self.head.prev = new_node
        new_node.next = self.head
        self.list_size += 1

    # 노드 선택
    def selectNode(self, idx):
        if self.list_size < idx:
            print("Overflow")
            return
        node = self.head
        count = 0
        while count < idx:
            node = node.next
            count += 1
        return node

    # 노드 삭제
    def deleteNode(self, idx):
        if self.list_size < 1:
            return
        elif self.list_size < idx:
            return

        if idx == 0:
            self.deleteHead()
            return
        node = self.selectNode(idx)
        node.prev.next = node.next
        node.next.prev = node.prev
        del node

    # 노드 헤드 삭제
    def deleteHead(self):
        node = self.head
        node.prev.next = node.next
        node.next.prev = node.prev
        self.head = node.next
        del node

    def size(self):
        return str(self.list_size)

if __name__ == "__main__":
    m_list = DoubleLinkedList(1)
    m_list.insertLast(5)
    m_list.insertLast(6)
    print('DLinkedList :', m_list)
    print('DLinkedList Size() :', m_list.size())
    print('DLinkedList SelectNode(2) :', m_list.selectNode(2))

    m_list.insertMiddleBefore(2, 12)
    print('DLinkedList InsertMiddleBefore(2, 12) :', m_list)

    m_list.insertFirst(100)
    print('DLinkedList InsertFirst(100) : ', m_list)
    print('DLinkedList SelectNode(0) :', m_list.selectNode(0))

    m_list.deleteNode(0)
    print('DLinkedList DeleteNode(0) : ', m_list)
    m_list.deleteHead()
    print('DLinkedList DeleteHead() : ', m_list)