class Node():
    def __init__(self):
        self.data = None
        self.next = None

def printNodes(start):
    cur = start
    if cur == None:
        return
    print(cur.data, end=' ')
    while cur.next != None:
        cur = cur.next
        print(cur.data, end=' ')
    print()

def insertNode(f_data, i_data):
    global memory, head, cur, pre

    # 처음
    if head.data == f_data:
        node = Node()
        node.data = i_data
        node.next = head
        head = node
        return

    # 중간
    cur = head
    while cur.next != None:
        pre = cur
        cur = cur.next
        if cur.data == f_data:
            node = Node()
            node.data = i_data
            node.next = cur
            pre.next = node
            return

    # 마지막
    node = Node()
    node.data = i_data
    cur.next = node

def delNode(d_data):
    global memory, head, cur, pre

    # 처음
    if head.data == d_data:
        cur = head
        head = head.next
        del(cur)
        return
    
    # 처음 외 나머지
    cur = head
    while cur.next != None:
        pre = cur
        cur = cur.next
        if cur.data == d_data:
            pre.next = cur.next
            del(cur)
            return

def findNode(f_data):
    global memory, head, cur, pre

    cur = head
    if cur.data == f_data:
        return cur
    while cur.next != None:
        cur = cur.next
        if cur.data == f_data:
            return cur
    return Node() # 빈 노드 반환

memory = []
head, pre, cur = None, None, None
dataArray = ["A", "B", "C", "D", "E"]

if __name__ == "__main__":
    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.next = node
        memory.append(node)

    printNodes(head)

    insertNode("A", "AA")
    printNodes(head)

    insertNode("C", "CC")
    printNodes(head)

    insertNode("H", "EE")
    printNodes(head)

    delNode("EE")
    printNodes(head)

    delNode("CC")
    printNodes(head)

    delNode("AA")
    printNodes(head)
    
    fNode = findNode("A")
    print(fNode.data)

    fNode = findNode("C")
    print(fNode.data)

    fNode = findNode("F")
    print(fNode.data)