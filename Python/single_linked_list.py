class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class SingleLinkedList:
    def __init__(self, data):
        new_node = Node(data)
        self.head = new_node
        self.list_size = 1

    def __str__(self):
        s_list = ''
        node = self.head
        while True:
            s_list += str(node)
            if node.next is None:
                break
            node = node.next
            s_list += '->'
        return s_list

    # 처음 노드 삽입
    def insertFirst(self, data):
        new_node = Node(data)       # 새 노드 생성
        temp_node = self.head       # 기존 헤드 임시 보관
        self.head = new_node        # 헤드를 새 노드로 변경
        self.head.next = temp_node  # 새로 생성된 헤드의 링크를 기존 헤드의 링크로 변경
        self.list_size += 1

    # 중간 노드 삽입
    def insertMiddle(self, idx, data):
        if self.head.next is None:  # 헤더를 만든 직후 메서드를 사용하는 경우
            self.insertLast(data)
            return
        node = self.selectNode(idx)
        new_node = Node(data)
        temp_next = node.next
        node.next = new_node
        new_node.next = temp_next
        self.list_size += 1

    # 마지막 노드 삽입
    def insertLast(self, data):
        node = self.head
        while True:
            if node.next is None:   # 다음 링크가 없으면
                break
            node = node.next
        new_node = Node(data)
        node.next = new_node        # 마지막 노드로 링크
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
        # 이전 노드의 링크를 다다음 노드와 연결하기 위해 이전 노드를 선택
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
    m_list = SingleLinkedList(1)
    m_list.insertLast(5)
    m_list.insertLast(6)
    print('LinkedList :', m_list)
    print('LinkedList Size() :', m_list.size())
    print('LinkedList SelectNode(2) :', m_list.selectNode(2))

    m_list.insertMiddle(1, 12)
    print('LinkedList InsertMiddle(1, 12) :', m_list)

    m_list.insertFirst(100)
    print('LinkedList InsertFirst(100) : ', m_list)
    print('LinkedList SelectNode(0) :', m_list.selectNode(0))

    m_list.deleteNode(0)
    print('LinkedList DeleteNode(0) : ', m_list)
    m_list.deleteHead()
    print('LinkedList DeleteHead() : ', m_list)