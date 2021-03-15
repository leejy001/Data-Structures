def isFull():
    global SIZE, queue, front, rear
    if (rear+1) % SIZE == front:
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
    rear = (rear+1) % SIZE
    queue[rear] = data

def deQueue():
    global SIZE, queue, front, rear
    if isEmpty():
        print("큐가 비었습니다.")
        return None
    front = (front+1)% SIZE
    data = queue[front]
    queue[front] = None
    return data

def calcTime():
    global SIZE, queue, front, rear
    timeSum = 0
    for i in range((front+1)%SIZE, (rear+1)%SIZE):
        timeSum += queue[i][1]
    return timeSum

SIZE = 6
queue = [None for _ in range(SIZE)]
front = rear = 0

if __name__ == "__main__":
    waitCall = [('use', 9), ('fix', 3), ('refund', 4), ('refund', 4), ('fix', 3)]

    for call in waitCall:
        print("예상 대기 시간", calcTime(), "분")
        print("현재 대기 콜 -->", queue)
        enQueue(call)
        print()

    print("최종 대기 콜 -->", queue)