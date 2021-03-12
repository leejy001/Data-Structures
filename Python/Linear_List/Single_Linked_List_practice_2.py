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

def makeSimpleLinkedList(data):
    global memory, head, cur, pre

    node = Node()
    node.data = data
    memory.append(node)

    # 처음 노드
    if head == None:
        head = node
        return

    # 처음 노드보다 작다면
    if head.data[0] > data[0]:
        node.next = head
        head = node
        return

    # 중간 삽입
    cur = head
    while cur.next != None:
        pre = cur
        cur = cur.next
        if cur.data[0] > data[0]:
            pre.next = node
            node.next = cur
            return

    # 삽입 노드가 제일 큰 경우
    cur.next = node

memory = []
head, pre, cur = None, None, None

if __name__ == "__main__":

    while True:
        name = input("이름-->")
        if name == '' or name == None:
            break
        phone = input("전화번호-->")
        makeSimpleLinkedList([name, phone])
        printNodes(head)