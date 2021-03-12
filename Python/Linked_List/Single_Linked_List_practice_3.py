import random

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

def makeLottoList(num):
    global memory, head, cur, pre

    node = Node()
    node.data = num
    memory.append(node)

    # 처음 노드
    if head == None:
        head = node
        return

    # 처음 노드보다 작다면
    if head.data > num:
        node.next = head
        head = node
        return

    # 중간 삽입
    cur = head
    while cur.next != None:
        pre = cur
        cur = cur.next
        if cur.data > num:
            pre.next = node
            node.next = cur
            return

    # 삽입 노드가 제일 큰 경우
    cur.next = node

def findNum(num):
    global memory, head, cur, pre

    if head == None:
        return False
    cur = head
    if cur.data == num:
        return True
    while cur.next != None:
        cur = cur.next
        if cur.data == num:
            return True
    return False

memory = []
head, pre, cur = None, None, None

if __name__ == "__main__":

    lottoCount = 0
    while True:
        lotto = random.randint(1, 45)
        if findNum(lotto):
            continue
        lottoCount += 1
        makeLottoList(lotto)
        if lottoCount >= 6:
            break

    printNodes(head)