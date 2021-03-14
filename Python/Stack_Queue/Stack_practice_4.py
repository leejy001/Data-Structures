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
        return
    top += 1
    stack[top] = data

def pop():
    global SIZE, stack, top
    if isEmpty():
        return None
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

SIZE = 100
stack = [None for _ in range(SIZE)]
top = -1

if __name__ == "__main__":
    with open("진달래꽃.txt", 'r', encoding='UTF8') as rfp:
        lineArray = rfp.readlines()

    print("----- 원본 -----")
    for line in lineArray:
        push(line)
        print(line, end=' ')
    print()

    print("----- 거꾸로 처리한 결과 -----")
    while True:
        line = pop()
        if line == None:
            break

        revStack = [None for _ in range(len(line))]
        revTop = -1

        for ch in line:
            revTop += 1
            revStack[revTop] = ch

        while True:
            if revTop == -1:
                break
            ch = revStack[revTop]
            revTop -= 1
            print(ch, end= '')