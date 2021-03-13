import random

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

def countOddEven():
    global memory, head, pre, cur

    odd, even = 0, 0
    if head == None:
        return False

    cur = head
    while True:
        if cur.data % 2 == 0:
            even += 1
        else:
            odd += 1
        if cur.next == head:
            break
        cur = cur.next
    return odd, even

def makeZeroNumber(odd, even):
    if odd > even:
        reminder = 1
    else:
        reminder = 0

    cur = head
    while True:
        if cur.data % 2 == reminder:
            cur.data *= -1
        if cur.next == head:
            break
        cur = cur.next

memory = []
head, pre, cur = None, None, None

if __name__ == "__main__":

    dataArray = []
    for _ in range(7):
        dataArray.append(random.randint(1, 100))

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

    oddCount, evenCount = countOddEven()
    print("홀수-->", oddCount, "\t", "짝수-->", evenCount)

    makeZeroNumber(oddCount, evenCount)
    printNodes(head)