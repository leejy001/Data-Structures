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

def peek():
    global SIZE, queue, front, rear
    if isEmpty():
        print("큐가 비었습니다.")
        return None
    return queue[(front+1)%SIZE]

SIZE = int(input("큐의 크기-->"))
queue = [None for _ in range(SIZE)]
front = rear = 0

if __name__ == "__main__":

    while True:
        select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택-->")

        if select == 'I' or select == 'i':
            data = input("입력할 데이터-->")
            enQueue(data)
            print("큐 상태 : ", queue)
        elif select == 'E' or select == 'e':
            data = deQueue()
            print("추출된 데이터 : ", data)
            print("큐 상태 : ", queue)
        elif select == 'V' or select == 'v':
            data = peek()
            print("확인된 데이터 : ", data)
            print("큐 상태 : ", queue)
        elif select == 'X' or select == 'x':
            print("종료...")
            break
        else:
            print("잘못된 입력 값")