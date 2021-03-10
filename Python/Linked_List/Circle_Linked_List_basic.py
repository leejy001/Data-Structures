class Node():
    def __init__(self):
        self.data = None
        self.next = None

def printNodes(start):
    cur = start
    if cur.next == None:
        return
    print(cur.data, end=' ')
    while cur.next != start:
        cur = cur.next
        print(cur.data, end=' ')
    print()

def insertNode(f_data, i_data):
    global memory, head, pre, cur

    # 첫 번째 노드 삽입
    if head.data == f_data:
        node = Node()
        node.data = i_data
        node.next = head
        last = head
        while last.next != head:
            last = last.next
        last.next = node
        head = node
        return

    # 중간 노드 삽입
    cur = head
    while cur.next != head:
        pre = cur
        cur = cur.next
        if cur.data == f_data:
            node = Node()
            node.data = i_data
            node.next = cur
            pre.next = node
            return

    # 마지막 노드 삽입
    node = Node()
    node.data = i_data
    cur.next = node
    node.next = head

def delNode(d_data):
    global memory, head, pre, cur

    # 첫 번째 노드 삭제
    if head.data == d_data:
        cur = head
        head = head.next
        last = head
        while last.next != cur:
            last = last.next
        last.next = head
        del(cur)
        return

    # 첫 번째 외 노드 삭제
    cur = head
    while cur.next != head:
        pre = cur
        cur = cur.next
        if cur.data == d_data:
            pre.next = cur.next
            del(cur)
            return

def findNode(f_data):
    global memory, head, pre, cur

    cur = head
    if cur.data == f_data:
        return cur

    while cur.next != head:
        cur = cur.next
        if cur.data == f_data:
            return cur

    return Node()

memory = []
head, pre, cur = None, None, None
dataArray = ["A", "B", "C", "D"]

if __name__ == "__main__":

    node = Node()
    node.data = dataArray[0]
    head = node
    node.next = head
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.next = node
        node.next = head
        memory.append(node)

    printNodes(head)

    insertNode("A", "AA")
    printNodes(head)

    insertNode("C", "CC")
    printNodes(head)

    insertNode("E", "E")
    printNodes(head)

    delNode("AA")
    printNodes(head)

    delNode("CC")
    printNodes(head)

    fNode = findNode("A")
    print(fNode.data)

    fNode = findNode("E")
    print(fNode.data)

    fNode = findNode("F")
    print(fNode.data)