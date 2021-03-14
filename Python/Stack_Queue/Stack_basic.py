def isFull():
    global SIZE, stack, top
    if top >= SIZE-1:
        return True
    else:
        return False

def isEmpty():
    global SIZE, stack, top
    if top == -1:
        return True
    else:
        return False

def push(data):
    global SIZE, stack, top
    if isFull():
        print("Stack is Full!")
        return
    else:
        top += 1
        stack[top] = data

def pop():
    global SIZE, stack, top
    if isEmpty():
        print("Stack is Empty!")
        return None
    else:
        data = stack[top]
        stack[top] = None
        top -= 1
        return data

def peek():
    global SIZE, stack, top
    if isEmpty():
        print("Stack is Empty!")
        return None
    return stack[top]

SIZE = int(input("스택의 크기-->"))
stack = [None for _ in range(SIZE)]
top = -1

if __name__ == "__main__":

    while True:
        select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택-->")

        if select == 'I' or select == 'i':
            data = input("입력할 데이터-->")
            push(data)
            print("스택 상태 : ", stack)
        elif select == 'E' or select == 'e':
            data = pop()
            print("추출된 데이터 : ", data)
            print("스택 상태 : ", stack)
        elif select == 'V' or select == 'v':
            data = peek()
            print("확인된 데이터 : ", data)
            print("스택 상태 : ", stack)
        elif select == 'X' or select == 'x':
            print("종료...")
            break
        else:
            print("잘못된 입력 값")