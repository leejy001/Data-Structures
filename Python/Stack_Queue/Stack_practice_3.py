import random

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

SIZE = 10
stack = [None for _ in range(SIZE)]
top = -1

if __name__ == "__main__":
    stones = ["red", "blue", "green", "yellow", "purple", "orange"]
    random.shuffle(stones)

    print("과자집에 가는 길 : 우리집 --> ", end=' ')
    for stone in stones:
        push(stone)
        print(stone, "-->", end=' ')
    print("과자집")

    print("우리집에 오는 길 : 과자집 --> ", end=' ')
    while True:
        stone = pop()
        if stone == None:
            break
        print(stone, "-->", end=' ')
    print("우리집")