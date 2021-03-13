import random
import math

class Node():
    def __init__(self):
        self.data = None
        self.next = None

def printStores(start):
    cur = start
    if cur == None:
        return

    while cur.next != head:
        cur = cur.next
        x, y = cur.data[1:]
        print(cur.data[0], '편의점, 거리 :',math.sqrt(x*x + y*y))
    print()

def makeStoreList(store):
    global memory, head, pre, cur

    node = Node()
    node.data = store
    memory.append(node)

    # 첫 번째 가게
    if head == None:
        head = node
        node.next = head
        return

    # 새 가게가 첫 번째 가게 보다 가까우면
    nX, nY = node.data[1:]
    nDist = math.sqrt(nX*nX + nY*nY)
    hX, hY = head.data[1:]
    hDist = math.sqrt(hX*hX + hY*hY)

    # 첫 편의점으로 만듬 (head 앞에 삽입)
    if hDist > nDist:
        node.next = head
        last = head
        while last.next != head:
            last = last.next
        last.next = node
        head = node
        return

    # 중간에 데이터를 넣을 경우
    cur = head
    while cur.next != head:
        pre = cur
        cur = cur.next
        curX, curY = cur.data[1:]
        curDist = math.sqrt(curX*curX + curY*curY)
        if curDist > nDist:
            pre.next = node
            node.next = cur
            return

    cur.next = node
    node.next = head

memory = []
head, pre, cur = None, None, None

if __name__ == "__main__":

    storeArray = []
    storeName = "A"

    for _ in range(10):
        store = (storeName, random.randint(1, 100), random.randint(1, 100))
        storeArray.append(store)
        storeName = chr(ord(storeName) + 1)

    for store in storeArray:
        makeStoreList(store)

    printStores(head)