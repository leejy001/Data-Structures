class Node():
    def __init__(self):
        self.data = None
        self.pnext = None   # 뒤쪽 링크
        self.nnext = None   # 앞쪽 링크

def printNodes(start):
    cur = start
    if cur.nnext == None:
        return
    print("정방향 -->", end=' ')
    print(cur.data, end=' ')
    while cur.nnext != None:
        cur = cur.nnext
        print(cur.data, end=' ')
    print()
    print("역방향 -->", end=' ')
    print(cur.data, end=' ')
    while cur.pnext != None:
        cur = cur.pnext
        print(cur.data, end=' ')

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
        pre.nnext = node
        node.pnext = pre
        memory.append(node)

    printNodes(head)