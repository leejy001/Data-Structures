def isFull():
    global SIZE, queue, front, rear
    if rear == SIZE - 1:
        return True
    else:
        return False

def isEmpty():
    global SIZE, queue, front, rear
    if front == rear:
        return True
    else:
        return False

def enQueue(data):
    global SIZE, queue, front, rear
    if isFull():
        print("큐가 꽉 찼습니다.")
        return
    rear += 1
    queue[rear] = data

def deQueue():
    global SIZE, queue, front, rear
    if isEmpty():
        print("큐가 비었습니다.")
        return None
    front += 1
    data = queue[front]
    queue[front] = None

    for i in range(front+1, rear+1):
        queue[i-1] = queue[i]
        queue[i] = None
    front = -1
    rear -= 1

    return data

def peek():
    global SIZE, queue, front, rear
    if isEmpty():
        print("큐가 비었습니다.")
        return None
    return queue[front + 1]

SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

if __name__ == "__main__":
    enQueue('A')
    enQueue('B')
    enQueue('C')
    enQueue('D')
    enQueue('E')
    print("대기 줄 상태 : ", queue)

    for _ in range(rear+1):
        print(deQueue(), "out..")
        print("대기 줄 상태 : ", queue)