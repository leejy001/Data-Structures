class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class CircleLinkedList:
    def __init__(self, data):
        new_node = Node(data)
        self.head = new_node
        self.tail = None
        self.list_size = 1

    def __str__(self):
        s_list = ''
        node = self.head
        while True:
            s_list += str(node)
            if node is self.tail:
                break
            node = node.next
            s_list += '->'
        return s_list

    # 노드 처음 삽입
    def insertFirst(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.tail = self.head
        temp_node = self.head
        self.head = new_node
        self.head.next = temp_node
        self.tail.next = new_node
        self.list_size += 1

    # 노드 중간 삽입
    def insertMiddle(self, idx, data):
        node = self.selectNode(idx)
        new_node = Node(data)
        temp_next = node.next
        node.next = new_node
        new_node.next = temp_next
        self.list_size += 1

    # 노드 마지막 삽입
    def insertLast(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.tail = new_node
            self.head.next = self.tail
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.tail.next = self.head
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
            return      # Underflow
        elif self.list_size < idx:
            return      # Overflow

        if idx == 0:
            self.deleteHead()
            return
        node = self.selectNode(idx - 1)
        node.next = node.next.next
        del_node = node.next
        del del_node

    # 헤드 노드 삭제
    def deleteHead(self):
        node = self.head
        self.head = node.next
        del node

    def size(self):
        return str(self.list_size)

if __name__ == "__main__":
    m_list = CircleLinkedList(1)
    m_list.insertLast(5)
    m_list.insertLast(6)
    print('CLinkedList :', m_list)
    print('CLinkedList Size() :', m_list.size())
    print('CLinkedList SelectNode(2) :', m_list.selectNode(2))

    m_list.insertMiddle(1, 12)
    print('CLinkedList InsertMiddle(1, 12) :', m_list)

    m_list.insertFirst(100)
    print('CLinkedList InsertFirst(100) : ', m_list)
    print('CLinkedList SelectNode(0) :', m_list.selectNode(0))

    m_list.deleteNode(0)
    print('CLinkedList DeleteNode(0) : ', m_list)
    m_list.deleteHead()
    print('CLinkedList DeleteHead() : ', m_list)